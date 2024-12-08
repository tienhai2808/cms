from .models import Topic, Post
from .services import RecentlyViewed
from django.db.models import Q
from datetime import datetime
from decouple import config
time_now = datetime.now().time()

def api_key(request):
  api_key = config('API_KEY')
  return {'api_key': api_key}

def topics(request):
  topics = Topic.objects.all()
  return {'topics': topics}

def recently_viewed(request):
  recently_viewed = RecentlyViewed(request)
  viewed_posts = recently_viewed.get_viewed_posts()
  return {'viewed_posts': viewed_posts}

def notification(request):
  if request.user.is_authenticated:
    user = request.user
    user_viewed = user.profile.recently_viewed
    if len(user_viewed) > 0:
      topics_of_viewed_posts = Post.objects.filter(id__in=user_viewed).values_list('section__topic', flat=True).distinct()
      related_posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now),
                                          section__topic__in=topics_of_viewed_posts, status='Đã đăng', posted_at__gte=user.date_joined
                                          ).exclude(id__in=user_viewed)
      new_notifications = [post.id for post in related_posts]
      user.profile.notification = list(dict.fromkeys(new_notifications + user.profile.notification))
      user.profile.save()
      notificated_posts = Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                                              id__in=user.profile.notification, status='Đã đăng').order_by('-posted_at')
      context = {'notificated_posts': notificated_posts}
    else:
      context = {'notificated_posts': None}
  else:
    context = {'notificated_posts': None}
  return context