from django.db import models

# Create your models here.


class ConfigItem(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)


class HistoryItem(models.Model):
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    dt_txt = models.CharField(max_length=255)
    dt = models.IntegerField()
    location = models.CharField(max_length=255)
