from pyexpat import model
from tokenize import detect_encoding
from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse_lazy
from .models import *
from TodoApp.forms import TaskForm
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

# Create your views here.

class TaskCreateView(CreateView):
 form_class = TaskForm
 template_name = 'TodoApp/task_create.html'
 success_url: reverse_lazy('home')

class TaskListView(ListView):
 template_name = 'TodoApp/task_list.html'
 queryset = Task.objects.all()
 context_object_name ='tasks'

class TaskDetailView(DetailView):
 model = Task
 template_name = 'TodoApp/task_detail.html'

class TaskUpdateView(UpdateView):
 model = Task
 template_name = 'TodoApp/task_Update.html'
 fields = '__all__'

class TaskDeleteView(DeleteView):
 model= Task
 template_name = 'TodoApp/task_confirm_delete.html'
 success_url = reverse_lazy('home')