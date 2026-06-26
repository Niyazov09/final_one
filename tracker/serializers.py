# from django.contrib.auth.models import User
# from rest_framework import serializers

# from .models import Project, Task, Comment


# class ProjectSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Project
#         fields = '__all__'


# class TaskSerializer(serializers.ModelSerializer):
#     assignee = serializers.PrimaryKeyRelatedField(
#         queryset=User.objects.all(),
#         required=False,
#         allow_null=True
#     )

#     class Meta:
#         model = Task
#         fields = '__all__'

#     def validate(self, attrs):
#         project = attrs.get(
#             "project",
#             getattr(self.instance, "project", None)
#         )

#         assignee = attrs.get("assignee")

#         if assignee and not project.is_member(assignee):
#             raise serializers.ValidationError({
#                 "assignee": [
#                     "Исполнитель должен быть участником проекта."
#                 ]
#             })

#         return attrs


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         model = Comment
#         fields = '__all__'






from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Project, Task, Comment


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'project',
            'title',
            'description',
            'status',
            'owner',
            'created_at'
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'text', 'created_at']