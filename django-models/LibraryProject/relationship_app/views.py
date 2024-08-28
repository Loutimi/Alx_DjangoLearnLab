from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.

def list_books(request):
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'
  context_object_name = 'library'
  queryset = Library.objects.all()
