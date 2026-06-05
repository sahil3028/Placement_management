from django.db import models

from applications.choices import ApplicationStatus
from jobs.models import JobPosting
from students.models import StudentProfile


class Application(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    job = models.ForeignKey(
        JobPosting,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    status = models.CharField(
        max_length=30,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.APPLIED,
        db_index=True,
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_at']
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'job'],
                name='unique_student_job_application',
            ),
        ]
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['student', 'status']),
            models.Index(fields=['job', 'status']),
            models.Index(fields=['applied_at']),
        ]

    def __str__(self):
        return f'{self.student.full_name} → {self.job.title} ({self.get_status_display()})'
