from django.contrib import admin
from .models import GrantAward, GrantAwardTask

@admin.register(GrantAward, GrantAwardTask)
class GrantAdmin(admin.ModelAdmin):
    pass