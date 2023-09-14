# from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

 path('task-create/',views.TaskCreateView.as_view(),name='task-create'),
 path('task-list/',views.TaskListView.as_view(),name='task-list'),

 path('<int:pk>/',views.TaskDetailView.as_view(), name='task-detail'),
 path('update/<int:pk>/',views.TaskUpdateView.as_view(), name='task-update'),
 path('delete/<int:pk>/',views.TaskDeleteView.as_view(), name='task-delete'),
]