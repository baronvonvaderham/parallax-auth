from django.db import models
from django.utils.translation import gettext_lazy as _

from parallax_auth.models.base import BaseModel
from parallax_auth.models.user import ParallaxUser


class Server(BaseModel):
    """
    Model for Server objects that represent remote servers
    which use this application to authenticate.
    """
    name = models.CharField(_('name'), max_length=32, blank=True, null=True)
    ip = models.GenericIPAddressField(_('IP Address'), blank=True, null=True, editable=False)

    owner = models.ForeignKey(ParallaxUser, blank=False, null=False, on_delete=models.CASCADE)
    authorized_users = models.ManyToManyField(ParallaxUser, blank=True, null=True, related_name='authorized_users')
