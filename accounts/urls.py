from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_choice_view, name='register'),
    path('register/student/', views.register_student_view, name='register_student'),
    path('register/recruiter/', views.register_recruiter_view, name='register_recruiter'),
]
