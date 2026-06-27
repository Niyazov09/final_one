from rest_framework.permissions import BasePermission


class IsProjectOwner(BasePermission):
    """
    Только владелец проекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsProjectMember(BasePermission):
    """
    Владелец или участник проекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.is_member(request.user)


class IsTaskProjectMember(BasePermission):
    """
    Доступ к задаче только участникам проекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.project.is_member(request.user)


class IsCommentProjectMember(BasePermission):
    """
    Доступ к комментариям только участникам проекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.task.project.is_member(request.user)


from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return hasattr(obj, "owner") and obj.owner == request.user


class IsOwnerOrMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, "owner"):
            return False

        return (
            obj.owner == request.user or
            obj.members.filter(id=request.user.id).exists()
        )


class IsTaskAssigneeOrProjectMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, "project"):
            return False

        return (
            obj.assignee == request.user or
            obj.project.owner == request.user or
            obj.project.members.filter(id=request.user.id).exists()
        )