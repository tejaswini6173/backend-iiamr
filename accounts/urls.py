from django.urls import path

from .views import (
    StaffListCreateView,
    StaffDetailView,
    StaffLoginView,
    StaffLogoutView,
    StaffTokenRefreshView,
)


urlpatterns = [
    path(
        "login/staff/login/",
        StaffLoginView.as_view(),
        name="staff-login",
    ),
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
    path(
        "login/logout/",
        StaffLogoutView.as_view(),
        name="staff-logout",
    ),
    path(
        "login/token/refresh/",
        StaffTokenRefreshView.as_view(),
        name="staff-token-refresh",
    ),
]