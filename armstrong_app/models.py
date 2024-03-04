# models.py
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add your additional fields

    # Set related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields as needed
    contact_number = models.CharField(max_length=15)

class UserAddress(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)



