from asyncio import tasks
from django.contrib import admin

from TodoApp.models import Task

# Register your models here.
admin.site.register(Task)
