from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """Permission to only allow admin users to POST/PUT/DELETE items"""

    message = "User is not an admin"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser
