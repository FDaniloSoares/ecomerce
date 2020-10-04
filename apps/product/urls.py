from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet, basename="categorias")
router.register(r"produtos", views.ProdutoViewSet, basename="produtos")

urlpatterns = [
    path("", include(router.urls)),
    
]