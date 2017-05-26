from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
# from django.db import models


class User(AbstractUser):
    data = JSONField(default={}, blank=True, null=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username
