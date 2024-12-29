from django.contrib import admin
from .models import BlogPost
from unfold.admin import ModelAdmin

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Display title and created_at in admin
    search_fields = ('title',)  # Allow searching by title

