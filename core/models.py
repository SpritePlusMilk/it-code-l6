from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)

