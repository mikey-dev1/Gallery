from unicodedata import name
from xmlrpc.client import Fault
from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
 name = models.CharField(max_length=100, unique=True)
 discription = models.TextField(max_length=512, blank=True, null=True)
 is_done = models.BooleanField(default=False)

 def get_absolute_url(self):
  return reverse("task-detail", args=[self.id])

 def __str__(self):
  return f'Task #{self.id}' 
