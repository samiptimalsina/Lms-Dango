from django.db import models
from courses.models import Courses  # Import the Courses model

class Units(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    document=models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='units')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
