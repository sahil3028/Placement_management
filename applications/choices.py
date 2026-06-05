from django.db import models


class ApplicationStatus(models.TextChoices):
    APPLIED = 'APPLIED', 'Applied'
    SHORTLISTED = 'SHORTLISTED', 'Shortlisted'
    INTERVIEW_SCHEDULED = 'INTERVIEW_SCHEDULED', 'Interview Scheduled'
    SELECTED = 'SELECTED', 'Selected'
    REJECTED = 'REJECTED', 'Rejected'