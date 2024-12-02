from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import post_save
from datetime import date
from django.utils.text import slugify

# Create your models here.

class Topic(models.Model):
  title = models.CharField(max_length=30)
  slug = models.SlugField()
  
  def __str__(self):
    return self.title
 
  
class Section(models.Model):
  title = models.CharField(max_length=50)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sections')
  slug = models.SlugField(blank=True, null=True)
  
  def __str__(self):
    return f'{self.topic} - {self.title}'

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Section, self).save(*args, **kwargs)
  

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avt = models.ImageField(upload_to='user_imgs/', default='user_imgs/default.png')
  phone = models.CharField(max_length=11, blank=True, null=True)
  gender = models.CharField(max_length=20, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Ẩn', 'Ẩn')], default='Ẩn')
  dob = models.DateField(blank=True, null=True)
  age_band = models.CharField(max_length=10, choices=[('Ẩn', 'Ẩn'), ('18-30', '18-30'), ('31-45', '31-45'), ('46-65', '46-65'), ('65+', '65+')], default='Ẩn')
  take_charge = models.ForeignKey(Topic, on_delete=models.SET_NULL, blank=True, null=True)
  about = models.CharField(max_length=1000, blank=True, null=True)
  recently_viewed = models.JSONField(default=list, blank=True, null=True) 
  
  @property
  def age(self):
    if self.dob:
      today = date.today()
      return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    return None
  
  def __str__(self):
    return self.user.username

  def calculate_age(self):
    if self.dob:
      age = self.age
      if 18 <= age <= 30:
        return '18-30'
      elif 31 <= age <= 45:
        return '31-45'
      elif 46 <= age <= 65:
        return '46-65'
      elif age >= 66:
        return '65+'
    return 'Ẩn'
  
  def save(self, *args, **kwargs):
    self.age_band = self.calculate_age()
    super(Profile, self).save(*args, **kwargs)
    
def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()
post_save.connect(create_profile, sender=User)


class Post(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_created')
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_updated', null=True, blank=True)
  title = models.CharField(max_length=500)
  image = models.ImageField(upload_to='thumbnails', default='thumbnails/default.jpg')
  body = CKEditor5Field('Text', config_name='extends')
  slug = models.SlugField(max_length=500)
  section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='posts')
  views = models.IntegerField(default=0)
  status = models.CharField(max_length=20, choices=[('Chờ gửi', 'Chờ gửi'), ('Chờ duyệt', 'Chờ duyệt'),('Từ chối', 'Từ chối'), ('Chờ sửa', 'Chờ sửa'), ('Chờ đăng', 'Chờ đăng'), ('Đã đăng', 'Đã đăng')], default='Chờ gửi')
  start_time = models.TimeField(blank=True, null=True)
  end_time = models.TimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  posted_at = models.DateTimeField(blank=True, null=True)
  
  def __str__(self):
    return self.title
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)


class Enjoy(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_enjoys')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_enjoys')
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    unique_together=('user','post')
  
  def __str__(self):
    return f'user {self.user.id} enjoy post {self.post.id}'
  
  
class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
  content = models.CharField(max_length=500)
  status = models.CharField(max_length=30, choices=[('Chờ duyệt', 'Chờ duyệt'), ('Đã duyệt', 'Đã duyệt')], default='Chờ duyệt')
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'user {self.user.id} comment post {self.post.id} at {self.created_at}'