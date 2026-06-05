from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import recruiter_required
from accounts.decorators import student_required
from applications.choices import ApplicationStatus
from applications.models import Application
from jobs.models import JobPosting


@student_required
def apply_job_view(request, job_id):
    student = request.user.student_profile

    job = get_object_or_404(
        JobPosting,
        pk=job_id,
    )

    application_exists = Application.objects.filter(
        student=student,
        job=job,
    ).exists()

    if application_exists:
        messages.warning(
            request,
            'You have already applied for this job.'
        )
        return redirect('jobs:detail', pk=job.pk)

    Application.objects.create(
        student=student,
        job=job,
        status=ApplicationStatus.APPLIED,
    )

    messages.success(
        request,
        'Application submitted successfully.'
    )

    return redirect('applications:list')


@student_required
def application_list_view(request):
    applications = (
        Application.objects
        .filter(student=request.user.student_profile)
        .select_related(
            'job',
            'job__company',
        )
        .order_by('-applied_at')
    )

    return render(
        request,
        'applications/application_list.html',
        {
            'applications': applications,
        }
    )


@recruiter_required
def update_application_status_view(
    request,
    application_id,
    status,
):
    application = get_object_or_404(
        Application,
        pk=application_id,
        job__company__created_by=request.user,
    )

    valid_statuses = [
        ApplicationStatus.SHORTLISTED,
        ApplicationStatus.INTERVIEW_SCHEDULED,
        ApplicationStatus.SELECTED,
        ApplicationStatus.REJECTED,
    ]

    if status not in valid_statuses:
        messages.error(
            request,
            'Invalid application status.'
        )
        return redirect('dashboard:recruiter')

    application.status = status
    application.save()

    messages.success(
        request,
        'Application status updated.'
    )

    return redirect('dashboard:recruiter')