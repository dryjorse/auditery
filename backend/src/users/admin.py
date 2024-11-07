from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
  model = User

# Register your models here.
