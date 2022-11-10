from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class AutocarueAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_filter = ['is_active']
    search_fields = ["title"]



@admin.register(Car)
class AutocarueAdmin(admin.ModelAdmin):
    list_display = ['title','image','category', 'description', 'date_create']
    list_filter = ['date_create']
    search_fields = ["title"]



