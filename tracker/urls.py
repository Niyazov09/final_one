from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

# 1. Создаем роутер для ViewSets
router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("tasks", TaskViewSet, basename="tasks")
router.register("comments", CommentViewSet, basename="comments")

# 2. Объявляем базовые пути (например, для JWT-токенов)
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# 3. Добавляем к общему списку пути из роутера
urlpatterns += router.urls