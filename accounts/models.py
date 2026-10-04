from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    CLASS_CHOICES = [
        (1, "Class 1"),
        (2, "Class 2"),
        (3, "Class 3"),
        (4, "Class 4"),
        (5, "Class 5"),
        (6, "Class 6"),
        (7, "Class 7"),
        (8, "Class 8"),
        (9, "Class 9"),
        (10, "Class 10"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    full_name = models.CharField(
        max_length=150
    )

    student_class = models.PositiveIntegerField(
        choices=CLASS_CHOICES
    )

    section = models.CharField(
        max_length=20,
        blank=True
    )

    school = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"{self.full_name} - Class {self.student_class}"