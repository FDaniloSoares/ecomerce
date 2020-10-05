from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet, basename="categorias")
router.register(r"produtos", views.ProdutoViewSet, basename="produtos")

urlpatterns = [
    path("", include(router.urls)),
]
