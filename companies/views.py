from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from accounts.decorators import recruiter_required
from companies.forms import CompanyForm
from companies.models import Company

COMPANIES_PER_PAGE = 10


def _recruiter_companies(user):
    return Company.objects.filter(created_by=user).select_related(
        'created_by__recruiter_profile',
    ).annotate(
        job_count=Count('jobs'),
    )


@recruiter_required
def company_list_view(request):
    companies = _recruiter_companies(request.user).order_by('-created_at')
    paginator = Paginator(companies, COMPANIES_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'companies/company_list.html', {
        'page_obj': page_obj,
        'active_nav': 'companies',
    })


@recruiter_required
@require_http_methods(['GET', 'POST'])
def company_create_view(request):
    form = CompanyForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        company = form.save(commit=False)
        company.created_by = request.user
        company.save()
        messages.success(request, f'Company "{company.company_name}" created successfully.')
        return redirect('companies:detail', pk=company.pk)

    return render(request, 'companies/company_form.html', {
        'form': form,
        'title': 'Create Company',
        'submit_label': 'Create Company',
        'active_nav': 'companies',
    })


@recruiter_required
def company_detail_view(request, pk):
    company = get_object_or_404(
        _recruiter_companies(request.user),
        pk=pk,
    )

    return render(request, 'companies/company_detail.html', {
        'company': company,
        'active_nav': 'companies',
    })


@recruiter_required
@require_http_methods(['GET', 'POST'])
def company_update_view(request, pk):
    company = get_object_or_404(Company, pk=pk, created_by=request.user)
    form = CompanyForm(request.POST or None, instance=company)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Company "{company.company_name}" updated successfully.')
        return redirect('companies:detail', pk=company.pk)

    return render(request, 'companies/company_form.html', {
        'form': form,
        'company': company,
        'title': 'Edit Company',
        'submit_label': 'Save Changes',
        'active_nav': 'companies',
    })


@recruiter_required
@require_http_methods(['GET', 'POST'])
def company_delete_view(request, pk):
    company = get_object_or_404(_recruiter_companies(request.user), pk=pk)

    if request.method == 'POST':
        name = company.company_name
        company.delete()
        messages.success(request, f'Company "{name}" deleted successfully.')
        return redirect('companies:list')

    return render(request, 'companies/company_confirm_delete.html', {
        'company': company,
        'active_nav': 'companies',
    })
