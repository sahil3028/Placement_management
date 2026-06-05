from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from accounts.forms import (
    LoginForm,
    RecruiterRegistrationForm,
    StudentRegistrationForm,
)


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, f'Welcome back, {form.get_user().username}!')
        return redirect('dashboard:home')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('accounts:login')


def register_choice_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    return render(request, 'accounts/register_choice.html')


@require_http_methods(['GET', 'POST'])
def register_student_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = StudentRegistrationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Student account created successfully!')
        return redirect('dashboard:student')

    return render(request, 'accounts/register_student.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def register_recruiter_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = RecruiterRegistrationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Recruiter account created successfully!')
        return redirect('dashboard:recruiter')

    return render(request, 'accounts/register_recruiter.html', {'form': form})
