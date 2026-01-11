from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete, PostListView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name="post-list"),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', post_create, name='post-create'),
    path('post/<int:id>/edit/', post_update, name='post-update'),
    path('post/<int:id>/delete/', post_delete, name='post-delete')
]
