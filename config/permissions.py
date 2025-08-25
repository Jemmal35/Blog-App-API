from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """
    Allows access only to admin or manager users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ['admin', 'manager']


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object or admins to edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj.author == request.user
