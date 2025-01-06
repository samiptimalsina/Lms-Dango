from django.db import models
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.TextField()
    site_keywords = models.CharField(max_length=255)
    site_email = models.EmailField()
    site_phone = models.CharField(max_length=20)
    site_address = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='site_logo')
    site_favicon = models.ImageField(upload_to='site_favicon')
    site_color=models.CharField(max_length=255)
    site_font=models.CharField(max_length=255)
    site_background=models.CharField(max_length=255)
    site_copyright = models.CharField(max_length=255)
    site_time_zone = models.CharField(max_length=255)
    site_currency = models.CharField(max_length=20)
    site_language = models.CharField(max_length=20)
    site_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.site_name
