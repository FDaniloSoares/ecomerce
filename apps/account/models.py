from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):

    name = models.CharField("Nome", max_length=120)

    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
