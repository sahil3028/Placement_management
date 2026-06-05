from django.urls import path

from applications import views

app_name = 'applications'

urlpatterns = [
    path('', views.application_list_view, name='list'),
    path('apply/<int:job_id>/', views.apply_job_view, name='apply'),
    path(
        '<int:application_id>/status/<str:status>/',
        views.update_application_status_view,
        name='update_status',
    ),
]