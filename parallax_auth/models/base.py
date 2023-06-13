from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Base class for all DB models to inherit from for consistency
    of applying fields and methods common to all DB tables.
    """
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
