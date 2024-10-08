from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
  path('books/', views.list_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
  path('register/', views.register, name='register'),
  path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html",next_page="home"), name="logout"),
  path("login/", LoginView.as_view(template_name="relationship_app/login.html",next_page="home"), name="login"),
  path('admin/', views.admin_view, name='admin_view'),
  path('librarian/', views.librarian_view, name='librarian_view'),
  path('member/', views.member_view, name='member_view'),
  
]
