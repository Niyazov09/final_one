from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Project, Task, Comment
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        u = self.request.user

        return Project.objects.filter(
            Q(owner=u) | Q(members=u)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"])
    def add_member(self, request, pk=None):
        project = self.get_object()

        if project.owner != request.user:
            raise PermissionDenied()

        user_id = request.data.get("user_id")

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=404
            )

        project.members.add(user)

        return Response({"status": "member added"})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = [
        "project",
        "status",
        "assignee"
    ]

    search_fields = ["title"]

    ordering_fields = [
        "priority",
        "created_at"
    ]

    def get_queryset(self):
        u = self.request.user

        return Task.objects.filter(
            Q(project__owner=u) |
            Q(project__members=u)
        ).distinct()

    def perform_create(self, serializer):
        project = serializer.validated_data["project"]

        if not project.is_member(self.request.user):
            raise PermissionDenied()

        serializer.save()

     


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.validated_data["task"]

        if not task.project.is_member(self.request.user):
            raise PermissionDenied()

        serializer.save(author=self.request.user)


from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "API работает"})        