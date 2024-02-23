from django.contrib import admin
from . models import Category
from .models import Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...



admin.site.register(Category, CategoryAdmin)