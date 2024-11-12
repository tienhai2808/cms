from django.utils.text import slugify
from myapp.models import Post

#Hàm xử lý trùng lặp slug
def generate_unique_slug(title):
  base_slug = slugify(title)
  slug = base_slug
  num = 1
  while Post.objects.filter(slug=slug).exists():
    slug = f"{base_slug}-{num}"
    num += 1
  return slug