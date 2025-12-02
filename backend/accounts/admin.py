from django.contrib import admin
from .models import PasswordHistory

@admin.register(PasswordHistory)
class PasswordHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "hashed_password", "created_at")
