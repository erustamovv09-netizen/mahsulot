from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahsulotViewSet

router = DefaultRouter()
router.register("mahsulot", MahsulotViewSet, basename="mahsulot")

urlpatterns = [
    path("", include(router.urls)),
]