from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'location', 'created_by', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('company_name', 'description', 'location')
    raw_id_fields = ('created_by',)
