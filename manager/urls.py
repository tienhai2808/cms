from django.urls import path
from .views import *

urlpatterns = [
    path('', pm_home, name='pm-home'),
    path('posts/', pm_post, name='pm-post'),
    path('employees/', pm_emp, name='pm-employee'),
    path('employees/<int:id_emp>/', pm_emp_detail, name='pm-employee-detail'),
    path('comments/', pm_cmt, name='pm-comment')
]