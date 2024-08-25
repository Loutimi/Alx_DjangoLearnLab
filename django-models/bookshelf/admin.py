from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Fields to display in the list view
    
    list_filter = ('author', 'publication_year')  # Fields to filter by in the admin interface
    
    search_fields = ('title', 'author')  # Fields to search in the admin interface

admin.site.register(Book, BookAdmin)