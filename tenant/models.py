from django.db import models
from django.db.models.base import Model

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length = 255)
    subdomain = models.CharField(max_length = 255)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete= models.CASCADE)

class Member(TenantAwareModel):
    name = models.CharField(max_length= 255)