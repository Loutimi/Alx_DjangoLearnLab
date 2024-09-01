from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')


# Register CustomUser and CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Register Book and BookAdmin.
admin.site.register(Book, BookAdmin)
