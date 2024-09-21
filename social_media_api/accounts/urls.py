# urls.py
from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, FeedView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name="follow"),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name="unfollow"),
    path('feed/', FeedView.as_view(), name='feed'),
]