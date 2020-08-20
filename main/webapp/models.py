from django.db import models


class RequestM(models.Model):
    name = models.CharField(max_length=1024)
    phone = models.CharField(max_length=64)
    info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

