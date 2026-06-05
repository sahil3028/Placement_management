from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.shortcuts import redirect, render

from accounts.choices import Role
from accounts.decorators import recruiter_required, student_required
from applications.models import Application
from applications.choices import ApplicationStatus
from companies.models import Company
from jobs.models import JobPosting
from students.models import StudentProfile
from recruiters.models import RecruiterProfile


@login_required
def home_view(request):
    if request.user.is_superuser or request.user.role == Role.ADMIN:
        return redirect('dashboard:admin')

    if request.user.role == Role.RECRUITER:
        return redirect('dashboard:recruiter')

    if request.user.role == Role.STUDENT:
        return redirect('dashboard:student')

    return redirect('accounts:login')


@student_required
def student_dashboard_view(request):
    profile = request.user.student_profile

    applications = (
        Application.objects
        .filter(student=profile)
        .select_related('job', 'job__company')
        .order_by('-applied_at')
    )

    context = {
        'profile': profile,
        'total_applications': applications.count(),
        'total_interviews': applications.filter(
            status=ApplicationStatus.INTERVIEW_SCHEDULED
        ).count(),
        'total_selected': applications.filter(
            status=ApplicationStatus.SELECTED
        ).count(),
        'total_rejected': applications.filter(
            status=ApplicationStatus.REJECTED
        ).count(),
        'recent_applications': applications[:5],
        'active_nav': 'dashboard',
    }

    return render(request, 'dashboard/student.html', context)


@recruiter_required
def recruiter_dashboard_view(request):
    profile = request.user.recruiter_profile

    companies = Company.objects.filter(
        created_by=request.user
    )

    jobs = JobPosting.objects.filter(
        company__created_by=request.user
    )

    applications = Application.objects.filter(
        job__company__created_by=request.user
    )

    context = {
        'profile': profile,
        'company_count': companies.count(),
        'job_count': jobs.count(),
        'applicant_count': applications.count(),
        'selected_count': applications.filter(
            status=ApplicationStatus.SELECTED
        ).count(),
        
        'recent_companies': companies.annotate(
            job_count=Count('jobs')
        ).order_by('-created_at')[:5],
        
        'recent_applications': applications.select_related(
    'student',
        'job',
        ).order_by('-applied_at')[:10],
       
        'active_nav': 'dashboard',
    }

    return render(request, 'dashboard/recruiter.html', context)


@login_required
def admin_dashboard_view(request):
    if request.user.role != Role.ADMIN and not request.user.is_superuser:
        messages.error(
            request,
            'You do not have permission to access this page.'
        )
        return redirect('dashboard:home')

    total_students = StudentProfile.objects.count()
    total_recruiters = RecruiterProfile.objects.count()
    total_companies = Company.objects.count()
    total_jobs = JobPosting.objects.count()
    total_applications = Application.objects.count()

    selected_count = Application.objects.filter(
        status=ApplicationStatus.SELECTED
    ).count()

    placement_rate = 0

    if total_applications:
        placement_rate = round(
            (selected_count / total_applications) * 100,
            2
        )

    context = {
        'total_students': total_students,
        'total_recruiters': total_recruiters,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'selected_count': selected_count,
        'placement_rate': placement_rate,
        'active_nav': 'dashboard',
    }

    return render(request, 'dashboard/admin.html', context)