# admin.py
from django.contrib import admin
from .models import CustomUser, UserProfile, UserAddress

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(UserAddress)
