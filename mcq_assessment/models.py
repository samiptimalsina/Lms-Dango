from django.db import models
from units.models import Units
from django.utils.translation import gettext_lazy as _  # For translations

class McqAssessment(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    options = models.JSONField(verbose_name=_("Options"))
    answer = models.TextField(verbose_name=_("Answer"))
    units = models.ForeignKey(Units, verbose_name=_("Unit"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
