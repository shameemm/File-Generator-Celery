from django.db import models

class TaskLog(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    args = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')