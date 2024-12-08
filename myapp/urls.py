from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='home'),   #Trang chủ
    path('register/', register, name='register'),   #Trang đăng ký
    path('login/', login, name='login'),   #Trang đăng nhập
    path('logout/', logout, name='logout'),   #Trang đăng xuất
    path('account/', account, name='account'),   #Trang tài khoản
    path('password-reset/', 
         views.PasswordResetView.as_view(template_name='client/pages/pr.html'), 
         name='password_reset'),   #Trang gửi thông báo lấy lại mật khẩu tới email
    path('password-reset-done/', 
         views.PasswordResetDoneView.as_view(template_name='client/pages/pr_done.html'), 
         name='password_reset_done'),   #Trang xác nhận đã gửi thông báo
    path('password-reset-confirm/<uidb64>/<token>/', 
         views.PasswordResetConfirmView.as_view(template_name='client/pages/pr_confirm.html'), 
         name='password_reset_confirm'),   #Trang lấy lại mật khẩu
    path('password-reset-complete/', 
         views.PasswordResetCompleteView.as_view(template_name='client/pages/pr_complete.html'), 
         name='password_reset_complete'),   #Trang lấy lại mật khẩu thành công
    path('posts/<slug:slug>/', post_detail, name='post-detail'),   #Trang bài viết đã đăng chi tiết
    path('update-profile/', update_profile, name='update-profile'),    #Trang chỉnh sửa hồ sơ
    path('update-profile/change-password/', change_password, name='change-password'),    #Trang đổi mật khẩu
    path('enjoyed/', enjoy_posts, name='enjoy'),   #Trang bài viết đã lưu
    path('search/', search, name='search'),   #Trang tìm kiếm
    path('weather/', weather, name='wearther'),   #Trang thời tiết
    path('<slug:slug_topic>/', topic, name='topic'),    #Trang các bài viết trong chủ đề
    path('<slug:slug_topic>/<slug:slug_section>/', section, name='section')   #Trang các bài viết trong danh mục
]