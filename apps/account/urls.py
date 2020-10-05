from django.urls import path
from rest_framework.authtoken import views

from apps.account.views import UserCreateAPIView

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="create-user"),
    path("api-token/", views.obtain_auth_token, name="api-token"),
]
