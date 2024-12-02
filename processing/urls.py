from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='pro-home'),   #Trang chủ xử lý bài viết
    path('drafts/', draft_list, name='draft-list'),    #Trang danh sách bản nháp của Contributor
    path('drafts/<slug:slug>/', draft_detail, name='draft-detail'),   #Trang bản nháp chi tiết
    path('posts/<slug:slug>/', post_detail, name='pro-post-detail'),   #Trang bài viết chi tiết (Chưa đăng)
    path('sections/', sections, name='sections'),   #Trang danh sách danh mục bài viết
    path('sections/<slug:slug>/', section, name='section'),   #Trang danh mục chi tiết
    path('create-draft/', create_draft, name='create-draft'),   #Trang tạo bản nháp của Contributor
    path('update-draft/<slug:slug>/', update_draft, name='update-draft'),   #Trang sửa bản nháp của Contributor
    path('update-post/<slug:slug>/', update_post, name='update-post'),   #Trang sửa bài viết của Editor
    path('list-edit/', list_edit, name='list-edit'),   #Trang danh sách bài viết chỉnh sửa của Editor
    path('pending-list/', pending_list, name='pending-list'),   #Trang danh sách bài viết chờ duyệt của Approver
    path('confirmation-list/', confirmation_list, name='confirmation-list')   #Trang danh sách bài viết chờ đăng của Approver
]