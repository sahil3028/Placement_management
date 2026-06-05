from django.urls import path

from students import views

app_name = "students"

urlpatterns = [
    path(
        "<int:pk>/",
        views.student_detail_view,
        name="detail",
    ),

    path(
        "profile/edit/",
        views.edit_profile_view,
        name="edit_profile",
    ),
]