from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views

urlpatterns = [
  path('books/', views.list_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
  path('register/', views.register, name='register'),
  path('login/', LoginView.as_view(template_name= 'relationship_app/login.html', next_page='home'), name='login'),
  path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html',next_page='home'), name='logout'),
]
