from django.conf import settings
from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, db_index=True)
    website = models.URLField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies',
        limit_choices_to={'role': 'RECRUITER'},
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'companies'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['company_name']),
            models.Index(fields=['location']),
            models.Index(fields=['created_by', 'created_at']),
        ]

    def __str__(self):
        return self.company_name
