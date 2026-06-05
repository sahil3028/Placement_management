from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('student/', views.student_dashboard_view, name='student'),
    path('recruiter/', views.recruiter_dashboard_view, name='recruiter'),
    path('admin/', views.admin_dashboard_view, name='admin'),
]
