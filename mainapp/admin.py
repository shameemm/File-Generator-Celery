from django.contrib import admin

# Register your models here.
from .models import TaskLog

admin.site.register(TaskLog)