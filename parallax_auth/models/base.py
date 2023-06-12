from django.db import models

import uuid


class BaseModel(models.Model):
    """
    Base class for all DB models to inherit from for consistency
    of applying fields and methods common to all DB tables.
    """

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
