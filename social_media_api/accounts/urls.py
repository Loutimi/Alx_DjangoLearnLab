from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, FollowViewSet, FeedView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
url = router.register(r'follow', FollowViewSet, basename='follow')

url = urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile"),

    # follow and unfollow route
    path('', include(url)),
    path('feed/', FeedView.as_view(), name='feed'),
]