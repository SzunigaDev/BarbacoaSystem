from django.db import models
from django.contrib.auth.models import User



class Status(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        related_name='%(class)s_created_by', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    updated_by = models.ForeignKey(
        User, 
        related_name='%(class)s_updated_by', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
