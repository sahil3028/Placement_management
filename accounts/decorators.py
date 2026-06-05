from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from accounts.choices import Role


def role_required(*allowed_roles):
    """Restrict view access to users with one of the given roles."""

    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                messages.error(
                    request,
                    'You do not have permission to access this page.',
                )
                return redirect('dashboard:home')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


student_required = role_required(Role.STUDENT)
recruiter_required = role_required(Role.RECRUITER)
admin_required = role_required(Role.ADMIN)
