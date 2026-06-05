from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
    )
    full_name = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField()
    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    phone_number = models.CharField(max_length=15)
    skills = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/%Y/%m/', blank=True, null=True)
    profile_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['college_name']),
            models.Index(fields=['branch']),
            models.Index(fields=['graduation_year']),
            models.Index(fields=['cgpa']),
        ]

    def __str__(self):
        return self.full_name

    @property
    def profile_completion_percentage(self):
        fields = [
            self.full_name,
            self.college_name,
            self.branch,
            self.graduation_year,
            self.cgpa,
            self.phone_number,
            self.skills,
            self.github_url,
            self.linkedin_url,
            self.resume,
        ]
        completed = sum(1 for field in fields if field not in (None, '', 0))
        return int((completed / len(fields)) * 100)
