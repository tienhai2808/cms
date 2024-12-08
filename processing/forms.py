from myapp.models import Post, Section
from django import forms

class EditorPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_by', 'updated_by', 'slug', 'view', 'status', 'start_time', 'end_time', 'posted_at', 'section']
    labels = {'title': 'Tiêu đề', 'image': 'Ảnh bài viết', 'body': 'Nội dung'}


class ContributorPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['created_by', 'updated_by', 'slug', 'view', 'status', 'start_time', 'end_time', 'posted_at']
    labels = {'title': 'Tiêu đề', 'image': 'Ảnh bài viết', 'body': 'Nội dung', 'section': 'Danh mục bài viết'}
 
  
class SectionForm(forms.ModelForm):
  class Meta:
    model = Section
    fields = ('title', 'topic')
    labels = {'title': 'Tên danh mục', 'topic': 'Chủ đề'}
    widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
               'topic': forms.Select(attrs={'class': 'form-select'})}
    