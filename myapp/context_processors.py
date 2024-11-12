from .models import Topic

def topics(request):
  topics = Topic.objects.all()
  return {'topics': topics}