from django.urls import path
from .views import *

urlpatterns = [
    path('', pm_home, name='pm-home'),
    path('posts/', pm_post, name='pm-post'),
    path('employees/', pm_emp, name='pm-employee'),
    path('comments/', pm_cmt, name='pm-comment')
]