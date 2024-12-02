from .models import Topic
from .services import RecentlyViewed

def topics(request):
  topics = Topic.objects.all()
  return {'topics': topics}

def recently_viewed(request):
  recently_viewed = RecentlyViewed(request)
  viewed_posts = recently_viewed.get_viewed_posts()
  return {'viewed_posts': viewed_posts}