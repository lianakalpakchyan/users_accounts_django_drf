from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'accounts'
        ordering = ['id']

    def __str__(self):
        return self.name
