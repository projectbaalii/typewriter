from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from base import views  # Import views from your app (replace 'base' with your app's name)
from base.models import BlogPost


# Define a custom admin site that requires OTP
class OTPAdmin(OTPAdminSite):
    pass

# Replace the default admin site with the custom OTPAdmin site
admin.site = OTPAdmin(name='admin')  # Override the default admin site
admin.site.register(User)
admin.site.register(TOTPDevice, TOTPDeviceAdmin)
admin.site.register(BlogPost)

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Use OTP-enabled admin site
    path('blogs/', views.blog_list, name='blog_list'),  # URL for blog list view
]
