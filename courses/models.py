from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField()
    description=models.CharField()
    price=models.IntegerField()
    duration=models.IntegerField()
    document=models.CharField()
    image=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
