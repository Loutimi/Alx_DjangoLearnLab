from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)  
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', null=True, blank=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='followed_by', blank=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='follows', blank=True)
