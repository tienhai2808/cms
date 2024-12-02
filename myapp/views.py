from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import auth, messages
from .forms import *
from .models import *
from .services import RecentlyViewed
from .utils import viewed_auth
from django.db.models import Q
from django.utils.text import slugify
from django.http import JsonResponse
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import PasswordChangeForm
time_now = datetime.now().time()

# Create your views here.
def register(request):
  if request.user.is_authenticated:
    return redirect('account')
  else:
    title = 'Đăng Ký'
    form_signup = SignUpForm(request.POST or None)
    if request.POST:
      if form_signup.is_valid():
        user = form_signup.save() 
        client_group = Group.objects.get(name='Client')
        user.groups.add(client_group)
        username = form_signup.cleaned_data['username'] 
        password = form_signup.cleaned_data['password1'] 
        user = auth.authenticate(username=username, password=password) 
        auth.login(request, user) 
        viewed_auth(request, user)
        messages.success(request, 'Mở Tài Khoản Thành Công') 
        return redirect('home')
      else:
        messages.error(request, 'Có Vấn Đề Xảy Ra, Vui Lòng Thử Lại')
        return redirect('register')
    return render(request, 'client/pages/register.html', {'title': title ,'form_signup': form_signup})

def login(request):
  if request.user.is_authenticated:
    return redirect('account')
  title = 'Đăng Nhập'
  if request.POST:
    username = request.POST.get('username') 
    password = request.POST.get('password') 
    user = auth.authenticate(username=username, password=password) 
    if user is not None: 
      auth.login(request,user)
      viewed_auth(request, user)
      return redirect('home')
    else: 
      messages.error(request,'Tài Khoản hoặc Mật Khẩu không đúng')
      return redirect('login')
  return render(request, 'client/pages/login.html', {'title': title})

def logout(request):
  auth.logout(request)
  return redirect('home')

def account(request):
  if request.user.is_authenticated:
    user = User.objects.get(id=request.user.id)
    title = f'{user.first_name} {user.last_name}'
    context = {'title': title,
               'user': user}
    return render(request, 'client/pages/account.html', context)
  else:
    return redirect('login')

def index(request):
  title = 'Báo VnExpress - Báo tiếng Việt nhiều người xem nhất'
  posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                              status='Đã đăng').order_by('-posted_at')[:30]
  paginator = Paginator(posts, 2)
  page_number = request.GET.get('page', '')
  try:
    page_obj = paginator.get_page(page_number)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginator.page(paginator.num_pages)
  context = {'title': title, 'page_obj': page_obj}
  return render(request, 'client/pages/home.html', context)

def topic(request, slug_topic):
  try:
    topic = Topic.objects.get(slug=slug_topic)
    posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now),
                                status='Đã đăng', section__topic=topic).order_by('-posted_at')
    title = topic.title
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page', '')
    try:
      page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
      page_obj = paginator.page(1)
    except EmptyPage:
      page_obj = paginator.page(paginator.num_pages)
    context = {'title': title,
               'page_obj': page_obj}
    return render(request, 'client/pages/topic.html', context)
  except Topic.DoesNotExist:
    return redirect('/')
  
def section(request, slug_topic, slug_section):
  try:
    section = Section.objects.get(slug=slug_section, topic__slug=slug_topic)
    posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                                status='Đã đăng', section=section).order_by('-posted_at')
    title = section.title
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page', '')
    try:
      page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
      page_obj = paginator.page(1)
    except EmptyPage:
      page_obj = paginator.page(paginator.num_pages)
    context = {'title': title,
               'page_obj': page_obj}
    return render(request, 'client/pages/section.html', context)
  except Section.DoesNotExist:
    return redirect('/')

def post_detail(request, slug):
  try:
    post = Post.objects.get(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                            status='Đã đăng', slug=slug)
    title = post.title
    post.views += 1
    post.save()
    comments = Comment.objects.filter(post=post, status='Đã duyệt')
    co_topic = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                                   status='Đã đăng', section__topic__title=post.section.topic.title
                                   ).exclude(slug=slug).order_by('?')[:11]
    recently_viewed = RecentlyViewed(request)
    recently_viewed.add(post.id)
    if request.user.is_authenticated:
      post.is_enjoyed = request.user.user_enjoys.filter(post=post).exists()
      if request.POST:
        cmt = request.POST.get('comment', '')
        if cmt:
          Comment.objects.create(user=request.user, post=post, content=cmt)
          messages.info(request, 'Đã gửi ý kiến, vui lòng chờ duyệt')
          return redirect('post-detail', slug)
        enjoy_content = request.POST.get('enjoy', '')
        if enjoy_content:
          enjoy, created = Enjoy.objects.get_or_create(user=request.user, post=post)
          if not created:
            enjoy.delete()
            return JsonResponse({'status': 'removed'})
          else:
            return JsonResponse({'status': 'added'}) 
    context = {'title': title, 'post': post, 'comments': comments, 'co_topic': co_topic}
    return render(request, 'client/pages/post_detail.html', context)
  except Post.DoesNotExist:
    return redirect('/')
    
def update_profile(request):
  if request.user.is_authenticated:
    title = 'Chỉnh sửa hồ sơ'
    form_u = UpdateUserForm(request.POST or None, instance=request.user)
    form_p = UpdateProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.POST:
      if form_u.is_valid() and form_p.is_valid():
        form_u.save()
        form_p.save()
        messages.success(request, 'Chỉnh sửa hồ sơ thành công')
        return redirect('account')
    context = {'title': title,
               'form_u': form_u,
               'form_p': form_p}
    return render(request, 'client/pages/update_profile.html', context)
  else:
    return redirect('home')
  
def change_password(request):
  title = 'Đổi mật khẩu'
  form = PasswordChangeForm(user=request.user, data=request.POST or None)
  form_errors = {}
  if request.POST:
    if form.is_valid():
      user = form.save()
      auth.update_session_auth_hash(request, user)
      messages.success(request, 'Đổi mật khẩu thành công')
      return redirect('account')
    else:
      form_errors = {field: error for field, errors in form.errors.items() for error in errors}
      if 'old_password' in form_errors:
        messages.error(request, 'Vui lòng nhập đúng mật khẩu hiện tại')
      elif 'new_password1' in form_errors or 'new_password2' in form_errors:
        messages.error(request, 'Mật khẩu mới không khớp hoặc không hợp lệ')
  context = {'title': title}
  return render(request, 'client/pages/cp.html', context)
  
def enjoy_posts(request):
  if request.user.is_authenticated:
    title = f'Bài viết đã lưu'
    enjoys = request.user.user_enjoys.filter(
      Q(post__start_time=None, post__end_time=None) | Q(post__start_time__lte=time_now, post__end_time__gte=time_now), 
      post__status='Đã đăng')
    context = {'title': title,
               'enjoys': enjoys}
    return render(request,'client/pages/enjoy_posts.html', context)
  else:
    return redirect('/')
  
def search(request):
  keyword = request.GET.get('q', '')
  if keyword:
    title = f"Kết quả tìm kiếm từ khóa '{keyword}'"
    posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                                Q(slug__icontains = slugify(keyword))|Q(body__icontains = keyword), status='Đã đăng'
                                ).order_by('-posted_at')
  else:
    title = 'Tìm kiếm bài viết'
    posts = None
  context = {'title': title, 'keyword': keyword, 'posts': posts}
  return render(request, 'client/pages/search.html', context)
  