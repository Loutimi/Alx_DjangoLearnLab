from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')


# Register CustomUser and CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Register Book and BookAdmin.
admin.site.register(Book, BookAdmin)
