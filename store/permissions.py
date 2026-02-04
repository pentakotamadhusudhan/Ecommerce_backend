from rest_framework.permissions import BasePermission


class IsVendor(BasePermission):
    def has_permission(self, request, view):
       
        return (
            request.user.is_authenticated and
            request.user.role == "VENDOR"
        )


class IsOwnerVendor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.vendor == request.user
