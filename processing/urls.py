from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='pro-home'),
    path('drafts/', draft_list, name='draft-list'),
    path('drafts/<slug:slug>/', draft_detail, name='draft-detail'),
    path('posts/<slug:slug>/', post_detail, name='pro-post-detail'),
    path('sections/', sections, name='sections'),
    path('sections/<slug:slug>/', section, name='section'),
    path('create-draft/', create_draft, name='create-draft'),
    path('update-draft/<slug:slug>/', update_draft, name='update-draft'),
    path('update-post/<slug:slug>/', update_post, name='update-post'),
    path('list-edit/', list_edit, name='list-edit'),
    path('pending-list/', pending_list, name='pending-list'),
    path('confirmation-list/', confirmation_list, name='confirmation-list')
]