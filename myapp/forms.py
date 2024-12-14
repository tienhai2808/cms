from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UpdateUserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')
    labels = {'first_name': 'Họ', 
              'last_name': 'Tên', 
              'email': 'Email'}


class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user', 'age_band', 'take_charge', 'recently_viewed', 'notification']
    widgets = {'dob': forms.DateInput(attrs={'type': 'date'}),}
    labels = {'avt': 'Ảnh đại diện', 
              'phone': 'Số điện thoại',
              'gender': 'Giới tính',
              'dob': 'Ngày sinh',
              'about': 'Giới thiệu'}
    

class SignUpForm(UserCreationForm):
  class Meta:
    model = User 
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    widgets = {'email': forms.TextInput(attrs={'placeholder': ' '}),
               'username': forms.TextInput(attrs={'placeholder': ' '}),
               'first_name': forms.TextInput(attrs={'placeholder': ' '}),
               'last_name': forms.TextInput(attrs={'placeholder': ' '})}
    labels = {'email': 'Email',
              'username': 'Tên đăng nhập',
              'first_name': 'Họ', 
              'last_name': 'Tên',}

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['password1'].widget.attrs['placeholder'] = ' '
    self.fields['password1'].label = 'Mật khẩu'
    self.fields['password1'].help_text = ''
    self.fields['password2'].widget.attrs['placeholder'] = ' '
    self.fields['password2'].label = 'Xác nhận mật khẩu'
    self.fields['password2'].help_text = ''