from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(
    upload_to='profile_images/', 
    default='default_images/default_profile.png'
)
    bio = models.TextField(
)