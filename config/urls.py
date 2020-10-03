from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include(("apps.product.urls", "product"), namespace="product")),
    path("account/", include(("apps.account.urls", "account"), namespace="account")),
    path("admin/", admin.site.urls),  
] 
