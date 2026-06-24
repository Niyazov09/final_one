from rest_framework.permissions import BasePermission


class IsProjectMember(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_member(request.user)


class IsProjectOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user