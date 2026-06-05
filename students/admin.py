from django.contrib import admin

from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'college_name', 'branch',
        'graduation_year', 'cgpa', 'profile_created',
    )
    list_filter = ('college_name', 'branch', 'graduation_year')
    search_fields = ('full_name', 'user__email', 'college_name', 'skills')
    raw_id_fields = ('user',)
