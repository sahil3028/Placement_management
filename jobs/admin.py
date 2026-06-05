from django.contrib import admin

from .models import JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'company', 'minimum_cgpa',
        'package_lpa', 'application_deadline', 'created_at',
    )
    list_filter = ('application_deadline', 'minimum_cgpa', 'package_lpa')
    search_fields = ('title', 'description', 'company__company_name')
    raw_id_fields = ('company',)
    date_hierarchy = 'application_deadline'
