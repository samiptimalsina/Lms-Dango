from django.db import models
from django.contrib.auth.models import User
from courses.models import Courses

class Enrollments(models.Model):
    enroll_date = models.DateField("Enrollment Date", auto_now=False, auto_now_add=False)
    enroll_expire_date = models.DateField("Enrollment Expire Date", auto_now=False, auto_now_add=False)
    users = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name="Course", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.users.username} - {self.course.name}"  # Assuming `username` and `name` exist
