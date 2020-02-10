from rest_framework import permissions


class IsAuthorOrSuperuser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user) or (request.user.is_superuser == True)


class IsAuthorOrStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user) or (request.user.is_staff == True)
