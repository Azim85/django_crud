from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete, PostListView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:id>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:id>/delete/', PostDeleteView.as_view(), name='post-delete')
]
