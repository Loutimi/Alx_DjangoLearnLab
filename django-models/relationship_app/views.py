from django.shortcuts import render, redirect
from django.db import models
from .models import Book 
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def list_books(request):
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'
  queryset = Library.objects.all()

# User authentication features
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
      user = form.save()
      login(request, user)
      return redirect('home')  
    
  else:
    form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')  
  else:
    form = AuthenticationForm()
  return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('home')

#  Adding a UserProfile model to store user roles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('Admin', 'Admin'),  
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Defining views that restrict access based on user roles.
@user_passes_test(lambda user: user.profile.role == 'Admin')
def admin_view(request):
    # Admin-specific content
    return render(request, 'admin_view.html')

@user_passes_test(lambda user: user.profile.role == 'Librarian')
def librarian_view(request):
    # Librarian-specific content
    return render(request, 'librarian_view.html')

@user_passes_test(lambda user: user.profile.role == 'Member')
def member_view(request):
    # Member-specific content
    return render(request, 'member_view.html')