from django.shortcuts import render, redirect
from .forms import *
from myapp.models import Post, Section, Topic
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from .utils import *

# Create your views here.  
@user_passes_test(in_group, login_url='/', redirect_field_name=None)
def index(request):
  title = 'CMS'
  context = {'title': title}
  return render(request,'processing/pages/home.html', context)

@user_passes_test(is_approver, login_url='/', redirect_field_name=None)
def sections(request):
  title = 'Danh mục bài viết'
  sections = Section.objects.all()
  form = SectionForm(request.POST or None)
  if request.POST:
    action = request.POST.get('action')
    if action == 'create':
      if form.is_valid():
        form.save()
        messages.success(request, 'Tạo danh mục thành công')
    else:
      id_section = request.POST.get('id_section')
      Section.objects.get(id=id_section).delete()
      messages.success(request, 'Xóa danh mục thành công')
    return redirect('sections')
  context = {'title': title,
             'sections': sections,
             'form': form}
  return render(request, 'processing/pages/sections.html', context)

@user_passes_test(is_approver, login_url='/', redirect_field_name=None)
def section(request, slug):
  try:
    section = Section.objects.get(slug=slug)
    title = section.title
    form = SectionForm(request.POST or None, instance=section)
    if request.POST:
      if form.is_valid():
        form.save()
        messages.success(request, 'Đã lưu chỉnh sửa')
        return redirect('sections')
    context = {'title': title,
                'form': form}
    return render(request, 'processing/pages/section.html', context)
  except Section.DoesNotExist:
    messages.warning(request, 'Không tìm thấy danh mục')
    return redirect('sections')

@user_passes_test(is_approver, login_url='/', redirect_field_name=None)
def pending_list(request):
  title = 'Danh sách chờ duyệt'
  posts = Post.objects.filter(status='Chờ duyệt')
  if request.POST:
    ids = request.POST.get('post-ids', '')  
    ids = [int(id.strip()) for id in ids.split(',') if id.strip().isdigit()]
    posts = posts.filter(id__in=ids)
    action = request.POST.get('action', '')
    for post in posts:
      post.status = 'Từ chối' if action == 'refuse' else 'Chờ sửa'
      post.save()
    messages.success(request, 'Đã từ chối những bản nháp đã chọn' if action == 'refuse' else 'Đã duyệt những bản nháp đã chọn')
    return redirect('pending-list')
  context = {'title': title,
              'posts': posts}
  return render(request, 'processing/pages/pending_list.html', context)

@user_passes_test(is_editor, login_url='/', redirect_field_name=None)
def list_edit(request):
  title = 'Danh sách chờ chỉnh sửa'
  if request.user.groups.filter(name='Approver').exists():
    posts = Post.objects.filter(status='Chờ sửa')
  else:
    posts = Post.objects.filter(section__topic=request.user.profile.take_charge, status='Chờ sửa')
  if request.POST:
    ids = request.POST.get('post-ids', '')  
    ids = [int(id.strip()) for id in ids.split(',') if id.strip().isdigit()]
    posts = posts.filter(id__in=ids)
    action = request.POST.get('action', '')
    if action == 'send':
      for post in posts:
        post.status = 'Chờ đăng'
        if not post.updated_by:
          post.updated_by = request.user
        post.save()
      messages.success(request, 'Đã gửi những bài viết đã chọn')
      return redirect('list-edit')
  context = {'title': title,
              'posts': posts}
  return render(request, 'processing/pages/list_edit.html', context)

@user_passes_test(is_contributor, login_url='/', redirect_field_name=None)
def draft_list(request):
  title = f'Danh sách bản nháp {request.user.username}'
  posts = Post.objects.filter(Q(status='Chờ gửi')|Q(status='Từ chối'), created_by = request.user)
  status = request.GET.get('status', '')
  if status == 'Chờ gửi':
    posts = posts.filter(status = 'Chờ gửi')
  if status == 'Từ chối':
    posts = posts.filter(status = 'Từ chối')
  if request.POST:
    ids = request.POST.get('post-ids', '')  
    ids = [int(id.strip()) for id in ids.split(',') if id.strip().isdigit()]
    posts = posts.filter(id__in=ids)
    action = request.POST.get('action', '')
    if action == 'send':
      for post in posts:
        post.status = 'Chờ duyệt'
        post.save()
    else:
      for post in posts:
        post.delete()
    messages.success(request, 'Đã xóa những bản nháp đã chọn' if action == 'delete' else 'Đã gửi những bản nháp đã chọn') 
    return redirect('draft-list')
  context = {'title':title,
              'posts':posts,
              'status': status}
  return render(request, 'processing/pages/draft_list.html', context)

@user_passes_test(is_contributor, login_url='/', redirect_field_name=None)
def draft_detail(request, slug):
  try:
    post = Post.objects.get(Q(status='Chờ gửi')|Q(status='Từ chối'), slug=slug, created_by=request.user)
    title = f'Bản nháp của {request.user.username}'
    if request.POST:
      action = request.POST.get('action', '')
      if action == 'delete':
        post.delete()
      else:
        post.status = 'Chờ duyệt'
        post.save()
      messages.success(request, 'Gửi bản nháp thành công' if action == 'send' else 'Xóa bản nháp thành công')
      return redirect('pro-home')
    context = {'post': post,
               'title': title}
    return render(request, 'processing/pages/draft_detail.html', context)
  except Post.DoesNotExist:
    messages.warning(request, 'Không tìm thấy bản nháp này')
    return redirect('pro-home')

@user_passes_test(is_editor, login_url='/', redirect_field_name=None)
def post_detail(request, slug):
  try:
    post = Post.objects.get(slug=slug)
    title = f'Bài viết số {post.id}'
    if request.POST:
      pending = request.POST.get('pending', '')
      if pending:
        post.status = 'Chờ sửa' if pending == 'accept' else 'Từ chối'
        post.save()
        messages.success(request, 'Duyệt bản nháp thành công' if pending == 'accept' else 'Từ chối bản nháp thành công')
      send = request.POST.get('send', '')
      if send:
        post.status = 'Chờ đăng'
        post.updated_by = request.user
        post.save()
        messages.success(request, 'Gửi bài viết thành công')
      action = request.POST.get('action', '')
      if action:
        if action == 'delete':
          post.delete()
          messages.success(request, 'Xóa bài viết thành công')
        if action == 'post':
          start_time = request.POST.get('start-time', '')
          end_time = request.POST.get('end-time', '')
          if start_time and end_time:
            post.start_time = start_time
            post.end_time = end_time
          post.status = 'Đã đăng'
          post.posted_at = timezone.now()
          post.save()
          messages.success(request, 'Đăng bài thành công')
      return redirect('pro-home')
    context = {'title': title,
              'post': post}
    return render(request, 'processing/pages/post_detail.html', context)
  except Post.DoesNotExist:
    messages.info(request, 'Bài viết đã bị xóa')
    return redirect('pro-home')

@user_passes_test(is_contributor, login_url='/', redirect_field_name=None)
def create_draft(request):
  form_cp = ContributorPostForm(request.POST or None, request.FILES or None)
  title = 'Tạo bản thảo'
  if request.POST:
    send = request.POST.get('send', '')
    if form_cp.is_valid():
      draft = form_cp.save(False)
      draft.created_by = request.user 
      if send:
        draft.status = 'Chờ duyệt'
      draft.save()
      messages.success(request, 'Tạo và gửi bản nháp thành công' if send else 'Tạo bản nháp thành công')       
      return redirect('pro-home')
  context = {'title': title, 'form_cp': form_cp}
  return render(request,'processing/pages/create_draft.html', context)

def update_draft(request, slug):
  try:
    draft = Post.objects.get(Q(status='Chờ gửi') | Q(status='Từ chối'), slug=slug, created_by=request.user)
    title = f'Sửa bản nháp của {request.user.username}'
    form_up = ContributorPostForm(request.POST or None, request.FILES or None, instance=draft)
    if request.POST:
      send = request.POST.get('send', '')
      if form_up.is_valid(): 
        draft = form_up.save(False)
        if send:
          draft.status = 'Chờ duyệt'
        draft.save()
        messages.success(request,'Đã gửi bản nháp cho Tổng biên tập' if send else 'Đã lưu chỉnh sửa bản nháp')
        return redirect('draft-list') if send else redirect('draft-detail', slug=draft.slug)
    context = {'title': title ,'form_up': form_up}
    return render(request, 'processing/pages/update_post.html', context)
  except Post.DoesNotExist:
    messages.warning(request, 'Không tìm thấy bản chỉnh sửa')
    return redirect('pro-home')

@user_passes_test(is_editor, login_url='/', redirect_field_name=None)
def update_post(request, slug):
  try:
    if request.user.groups.filter(name='Approver').exists():
      post = Post.objects.get(Q(status='Chờ sửa') | Q(status='Chờ đăng'), slug=slug)
    else:
      post = Post.objects.get(slug=slug, section__topic=request.user.profile.take_charge, status='Chờ sửa')
    title = f'Sửa bài viết số {post.id}'
    form_up = EditorPostForm(request.POST or None,request.FILES or None, instance=post)
    if request.POST:
      send = request.POST.get('send', '')
      if form_up.is_valid(): 
        post = form_up.save(False)
        if send:
          post.status = 'Chờ đăng'
        if not post.updated_by:
          post.updated_by = request.user
        post.save() 
        messages.success(request, 'Đã gửi bài viết cho Tổng biên tập' if send else 'Đã lưu chỉnh sửa')
        return redirect('list-edit') if send else redirect('pro-post-detail', slug)
    context = {'title': title, 
               'form_up': form_up, 
               'post': post}
    return render(request, 'processing/pages/update_post.html', context)
  except Post.DoesNotExist:
    messages.warning(request, 'Không tìm thấy bản chỉnh sửa')
    return redirect('pro-home')

@user_passes_test(is_approver, login_url='/', redirect_field_name=None)  
def confirmation_list(request):
  title = 'Danh sách chờ đăng'
  posts = Post.objects.filter(status='Chờ đăng')
  if request.POST:
    ids = request.POST.get('post-ids', '')  
    ids = [int(id.strip()) for id in ids.split(',') if id.strip().isdigit()]
    posts = posts.filter(id__in=ids)
    action = request.POST.get('action', '')
    if action == 'delete':
      for post in posts:
        post.delete()
    else:
      start_time = request.POST.get('start_time', '')
      end_time = request.POST.get('end_time', '')
      for post in posts:
        if start_time and end_time:
          post.start_time = start_time
          post.end_time = end_time
        post.status = 'Đã đăng'
        post.posted_at = timezone.now()
        post.save()
    messages.success(request,'Xóa thành công các bài viết đã chọn' if action == 'delete' else 'Đã đăng bài viết đã chọn lên trang chủ')
    return redirect('confirmation-list')
  context = {'title': title,
              'posts': posts}
  return render(request, 'processing/pages/confirmation_list.html', context)