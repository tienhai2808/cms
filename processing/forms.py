from myapp.models import Post, Section
from .models import Request
from django import forms

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_by', 'updated_by', 'slug', 'views', 'status', 'start_time', 'end_time', 'posted_at']
    labels = {'title': 'Tiêu đề', 'image': 'Ảnh bài viết', 'body': 'Nội dung', 'section': 'Thẻ bài viết'}
  
class SectionForm(forms.ModelForm):
  class Meta:
    model = Section
    fields = ('title', 'topic')
    
class RequestForm(forms.ModelForm):
  class Meta:
    model = Request
    fields = ('content',)