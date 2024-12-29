from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice
from tinymce.models import HTMLField


class MyTOTPDevice(TOTPDevice):
    """
    Custom TOTPDevice class to mark it as always interactive.
    """
    @property
    def is_interactive(self):
        """
        Indicates that the TOTP device is always interactive.
        """
        return True


class BlogPost(models.Model):
    """
    BlogPost model with a title, rich text content, and a timestamp for creation.
    """
    title = models.CharField(
        max_length=200, 
        help_text="Enter the title of the blog post."
    )
    content = HTMLField(
        help_text="Write the content of the blog post here."
    )  # Adds TinyMCE editor
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time this post was created."
    )

    def __str__(self):
        """
        Returns the string representation of the BlogPost, which is its title.
        """
        return self.title


class MyModel(models.Model):
    """
    A simple model with a name and description.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """
        Returns the string representation of MyModel, which is its name.
        """
        return self.name
