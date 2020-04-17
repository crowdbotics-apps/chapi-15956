from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CHdbViewSet

router = DefaultRouter()
router.register("chdb", CHdbViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
