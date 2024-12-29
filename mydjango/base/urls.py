# from django.urls import path
# from . import views

# urlpatterns = [
#     path('create/', views.create_blog_post, name='create_blog_post'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('blogs/', views.blog_list, name='blog_list'),
    
# ]

# main/urls.py
from unfold.admin import AdminSite  # Custom admin site if using Unfold package
from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current directory

# Initialize the custom admin site
admin.site = AdminSite()

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.blog_list, name='base_list'),  # Base URL for the blog list view
]

