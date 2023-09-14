from ast import mod
from dataclasses import field, fields
from django.forms import ModelForm
from ImageApp import forms

from ImageApp.models import Book, UserInfo
from .models import *

class TaskForm(ModelForm):
 class Meta:
  model = Task
  fields = '__all__'

class BookCreateForm(ModelForm):
 class Meta:
  model = Book
  fields = '__all__'

from django import forms
class ConfirmForm(forms.Form):
 confirm = forms.BooleanField(label = 'Confirm')

from django.forms import ModelForm
class UserForm(ModelForm):
 class Meta:
  model = UserInfo
  fields = '__all__'  