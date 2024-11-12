from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('account/', account, name='account'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='client/pages/pr.html'), name='password_reset'),
    path('password-reset-done/', views.PasswordResetDoneView.as_view(template_name='client/pages/pr_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='client/pages/pr_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(template_name='client/pages/pr_complete.html'), name='password_reset_complete'),
    path('post/<slug:slug>/', post_detail, name='post-detail'),
    path('update-profile/', update_profile, name='update-profile'),
    path('update-profile/change-password/', change_password, name='change-password'),
    path('enjoyed/', enjoy_posts, name='enjoy'),
    path('search/', search, name='search'),
    path('<slug:slug_topic>/', topic, name='topic'),
    path('<slug:slug_topic>/<slug:slug_section>/', section, name='section')
]