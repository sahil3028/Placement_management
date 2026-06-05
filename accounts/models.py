from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import Role
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        db_index=True,
    )

    objects = UserManager()

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role', 'is_active']),
        ]

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    @property
    def is_student(self):
        return self.role == Role.STUDENT

    @property
    def is_recruiter(self):
        return self.role == Role.RECRUITER

    @property
    def is_placement_admin(self):
        return self.role == Role.ADMIN
