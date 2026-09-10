from django.urls import path

from .views import (
    StaffListCreateView,
    StaffDetailView,
    StaffLoginView,
)


urlpatterns = [
    # Staff login
    path(
        "login/staff/login/",
        StaffLoginView.as_view(),
        name="staff-login",
    ),

    # Staff management
    path(
        "login/staff/",
        StaffListCreateView.as_view(),
        name="staff-list-create",
    ),

    path(
        "login/staff/<int:pk>/",
        StaffDetailView.as_view(),
        name="staff-detail",
    ),
]