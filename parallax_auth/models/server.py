from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from oauth2_provider.models import AbstractApplication

from parallax_auth.models.base import BaseModel
from parallax_auth.models.user import ParallaxUser


class ServerManager(models.Manager):
    pass


class Server(BaseModel, AbstractApplication):
    """
    Model for Server objects that represent remote servers
    which use this application to authenticate.
    """
    name = models.CharField(_('name'), max_length=32, blank=False, null=False)
    ip = models.GenericIPAddressField(_('IP Address'), blank=True, null=True, editable=False)

    authorized_users = models.ManyToManyField(ParallaxUser, blank=True, null=True, related_name='authorized_users')

    objects = ServerManager()

    class Meta:
        # Owner cannot have multiple servers with the same name
        unique_together = [['name', 'user']]

    def __str__(self):
        return self.name
