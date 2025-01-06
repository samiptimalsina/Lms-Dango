
from django.db import models

class BannerImage(models.Model):
        banner_image = models.ImageField(upload_to='banner_image')
        status=models.BooleanField(default=True)
        banner_title=models.TextField(null=True)
        banner_description=models.TextField(null=True)
        banner_link=models.CharField(max_length=255,null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.banner_image
