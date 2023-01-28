from django.db import models



class TaskLog(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, default='')
    args = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')