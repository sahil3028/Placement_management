from django.contrib import admin

from .models import RecruiterProfile


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('recruiter_name', 'designation', 'phone_number')
    search_fields = ('recruiter_name', 'user__email')
    raw_id_fields = ('user',)
