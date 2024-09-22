from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

posts_url = urlpatterns = router.urls

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name="like_post"),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('', include(posts_url)),
]