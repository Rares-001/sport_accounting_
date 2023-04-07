from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('bar_category_name',)}
    list_display = ('bar_category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
