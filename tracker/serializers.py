from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Task, Comment


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, attrs):
        project = attrs.get(
            "project",
            getattr(self.instance, "project", None)
        )

        assignee = attrs.get("assignee")

        if assignee and not project.is_member(assignee):
            raise serializers.ValidationError({
                "assignee": [
                    "Исполнитель должен быть участником проекта."
                ]
            })

        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'