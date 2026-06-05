from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import recruiter_required
from companies.models import Company
from jobs.forms import JobPostingForm
from jobs.models import JobPosting


def job_list_view(request):
    jobs = (
        JobPosting.objects
        .select_related('company')
        .all()
        .order_by('-created_at')
    )

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs,
        }
    )


def job_detail_view(request, pk):
    job = get_object_or_404(
        JobPosting.objects.select_related('company'),
        pk=pk,
    )

    return render(
        request,
        'jobs/job_detail.html',
        {
            'job': job,
        }
    )


@recruiter_required
def job_create_view(request):
    form = JobPostingForm(
        request.POST or None
    )

    form.fields['company'].queryset = Company.objects.filter(
        created_by=request.user
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        messages.success(
            request,
            'Job posting created successfully.'
        )

        return redirect('jobs:list')

    return render(
        request,
        'jobs/job_form.html',
        {
            'form': form,
            'title': 'Create Job',
        }
    )


@recruiter_required
def job_update_view(request, pk):
    job = get_object_or_404(
        JobPosting,
        pk=pk,
        company__created_by=request.user,
    )

    form = JobPostingForm(
        request.POST or None,
        instance=job,
    )

    form.fields['company'].queryset = Company.objects.filter(
        created_by=request.user
    )

    if request.method == 'POST' and form.is_valid():
        form.save()

        messages.success(
            request,
            'Job updated successfully.'
        )

        return redirect('jobs:detail', pk=job.pk)

    return render(
        request,
        'jobs/job_form.html',
        {
            'form': form,
            'title': 'Edit Job',
        }
    )


@recruiter_required
def job_delete_view(request, pk):
    job = get_object_or_404(
        JobPosting,
        pk=pk,
        company__created_by=request.user,
    )

    if request.method == 'POST':
        job.delete()

        messages.success(
            request,
            'Job deleted successfully.'
        )

        return redirect('jobs:list')

    return render(
        request,
        'jobs/job_confirm_delete.html',
        {
            'job': job,
        }
    )