from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import home

from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('', home),
]


from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls



from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls