from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts.decorators import recruiter_required
from accounts.decorators import student_required
from students.forms import StudentProfileForm
from students.models import StudentProfile


@recruiter_required
def student_detail_view(request, pk):
    student = get_object_or_404(
        StudentProfile,
        pk=pk,
    )

    return render(
        request,
        "students/student_detail.html",
        {
            "student": student,
        },
    )


@student_required
def edit_profile_view(request):
    profile = request.user.student_profile

    form = StudentProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Profile updated successfully."
        )

        return redirect("dashboard:student")

    return render(
        request,
        "students/edit_profile.html",
        {
            "form": form,
        },
    )