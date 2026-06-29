# from rest_framework.permissions import BasePermission


# class IsProjectOwner(BasePermission):
#     """
#     Только владелец проекта.
#     """

#     def has_object_permission(self, request, view, obj):
#         return obj.owner == request.user


# class IsProjectMember(BasePermission):
#     """
#     Владелец или участник проекта.
#     """

#     def has_object_permission(self, request, view, obj):
#         return obj.is_member(request.user)


# class IsTaskProjectMember(BasePermission):
#     """
#     Доступ к задаче только участникам проекта.
#     """

#     def has_object_permission(self, request, view, obj):
#         return obj.project.is_member(request.user)


# class IsCommentProjectMember(BasePermission):
#     """
#     Доступ к комментариям только участникам проекта.
#     """

#     def has_object_permission(self, request, view, obj):
#         return obj.task.project.is_member(request.user)


# from rest_framework.permissions import BasePermission


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return hasattr(obj, "owner") and obj.owner == request.user


# class IsOwnerOrMember(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if not hasattr(obj, "owner"):
#             return False

#         return (
#             obj.owner == request.user or
#             obj.members.filter(id=request.user.id).exists()
#         )


# class IsTaskAssigneeOrProjectMember(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if not hasattr(obj, "project"):
#             return False

#         return (
#             obj.assignee == request.user or
#             obj.project.owner == request.user or
#             obj.project.members.filter(id=request.user.id).exists()
#         )



from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProjectOwner(BasePermission):
    """
    Только владелец проекта может изменять и удалять проект.
    Читать могут все участники проекта.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.is_member(request.user)

        return obj.owner == request.user


class IsProjectMember(BasePermission):
    """
    Доступ к проекту только владельцу и участникам.
    """

    def has_object_permission(self, request, view, obj):
        return obj.is_member(request.user)


class IsTaskProjectMember(BasePermission):
    """
    Доступ к задачам только участникам проекта.
    """

    def has_object_permission(self, request, view, obj):
        return obj.project.is_member(request.user)


class IsCommentProjectMember(BasePermission):
    """
    Читать комментарии могут участники проекта.
    Изменять и удалять комментарий может только его автор.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.task.project.is_member(request.user)

        return obj.author == request.user