from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from companies.models import Company


class JobPosting(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    minimum_cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    package_lpa = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['application_deadline']),
            models.Index(fields=['minimum_cgpa']),
            models.Index(fields=['package_lpa']),
            models.Index(fields=['company', 'created_at']),
        ]

    def __str__(self):
        return f'{self.title} — {self.company.company_name}'

    def clean(self):
        super().clean()
        if self.application_deadline and self.application_deadline < timezone.now().date():
            raise ValidationError({
                'application_deadline': 'Application deadline cannot be in the past.',
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def is_active(self):
        return self.application_deadline >= timezone.now().date()
