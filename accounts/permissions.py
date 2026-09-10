from rest_framework.permissions import BasePermission


class IsAdminStaff(BasePermission):
    """
    Allows access only to active staff members
    whose role is admin.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and getattr(request.user, "role", None) == "admin"
            and getattr(request.user, "status", None) == "active"
        )