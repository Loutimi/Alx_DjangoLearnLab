from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register, Login, ProfileView, NewPost, Posts, PostDetail, PostEdit, PostDelete, CommentCreateView, CommentDeleteView, CommentUpdateView, PostByTagListView, search

urlpatterns = [
    path('register/', Register.as_view(), name="regiser"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView, name="profile"),

    path('posts/', Posts.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostEdit.as_view(), name="post_edit"),
    path('post/new/', NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name="post_delete"),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag_posts'),
    path('search/', search, name='search'),
]