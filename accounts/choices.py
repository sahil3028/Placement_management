from django.db import models


class Role(models.TextChoices):
    STUDENT = 'STUDENT', 'Student'
    RECRUITER = 'RECRUITER', 'Recruiter'
    ADMIN = 'ADMIN', 'Admin'
