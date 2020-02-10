from rest_framework import permissions


class IsAuthorOrSuperuser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.username == request.user.username) or (request.user.is_superuser == True)
