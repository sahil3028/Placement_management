from django.conf import settings
from django.db import models


class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recruiter_profile',
    )
    recruiter_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    class Meta:
        indexes = [
            models.Index(fields=['recruiter_name']),
        ]

    def __str__(self):
        return self.recruiter_name
