from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    message = "No eres superusuario."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class ModelPermissionRequired(BasePermission):
    def has_permission(self, request, view):
        perm_dict = view.model_permission_dict or {}
        permission = perm_dict.get(request.method)
        return request.user.has_perm(permission)
