from .models import Post
from django.db.models import Case, When, Q
from datetime import datetime
time_now = datetime.now().time()

class RecentlyViewed:
  def __init__(self, request):
    self.session = request.session
    self.request = request
    self.recently_viewed = self.session.get('recently_viewed', [])  
    self.user = request.user if request.user.is_authenticated else None 
    
  def add(self, post_id):
    post_id = int(post_id)
    if post_id in self.recently_viewed:
      self.recently_viewed.remove(post_id)
    self.recently_viewed.append(post_id)
    if len(self.recently_viewed) > 10:
      self.recently_viewed.pop(0)  
    self.session['recently_viewed'] = self.recently_viewed
    if self.user:
      profile = self.user.profile
      profile.recently_viewed = self.recently_viewed
      profile.save()
    self.session.modified = True
      
  def get_viewed_posts(self):
    post_ids = [int(id) for id in self.recently_viewed]
    posts= Post.objects.filter(Q(start_time=None, end_time=None) | Q(start_time__lte=time_now, end_time__gte=time_now), 
                               id__in=post_ids, status='Đã đăng'
                               ).order_by(-Case(*[When(id=pk, then=pos) for pos, pk in enumerate(post_ids)]))
    return posts