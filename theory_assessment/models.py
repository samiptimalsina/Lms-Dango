from django.db import models

from units.models import Units
# Create your models here.
class TheoryAssessment(models.Model):
    units_id = models.ForeignKey(Units, on_delete=models.CASCADE)
    questions=models.TextField()
    answers=models.TextField()
    document=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
