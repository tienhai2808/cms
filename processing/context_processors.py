from myapp.models import Post

def len_list(request):
  pending_list_count = Post.objects.filter(status='Chờ duyệt').count()
  confirmation_list_count = Post.objects.filter(status='Chờ đăng').count()
  list_edit_count = Post.objects.filter(status='Chờ sửa').count()
  if request.user.is_authenticated:
    my_list_edit_count = Post.objects.filter(section__topic=request.user.profile.take_charge, status='Chờ sửa').count()
  else:
    my_list_edit_count = 0
  return {'pending_list_count': pending_list_count, 
          'confirmation_list_count': confirmation_list_count, 
          'list_edit_count': list_edit_count,
          'my_list_edit_count': my_list_edit_count}