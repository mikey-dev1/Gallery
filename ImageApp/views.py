# from ast import Delete
# from typing import ValuesView
# from urllib import request
from stat import FILE_ATTRIBUTE_COMPRESSED
from unicodedata import name
from urllib import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import View
# Create your views here.
def home(request):
 data = Profile.objects.all()
 return render(request,'ImageApp/home.html',{'data':data})

def Create_Team(request):
 if request.method == 'POST':
  form = TeamForm(request.POST,request.FILES)
  if form.is_valid():
   form.save()
   return redirect('team_success')
 form = TeamForm()
 return render(request,'ImageApp/create.html',{'form':form})

def Team_success(request):
 return render(request,'ImageApp/team_success.html') 

class BookListView(View):
 def get(self,request,*args,**kwargs):
  books = Book.objects.all()
  return render(request,'ImageApp/book-list.html',{'books':books})
  
class BookCreate(View):
 def get(self,request,*args,**kwargs):
  form = BookCreateForm()
  return render(request,'ImageApp/book-create.html',{'form':form})
 def post(self,request,*args,**kwargs):
  form = BookCreateForm(request.POST,request.FILES)
  if form.is_valid():
    form.save()
    return redirect('book-list')
  return render(request,'ImageApp/book-create.html',{'form':form})

class BookDetail(View):
 def get(self,request,*args,**kwargs):
  book = Book.objects.get(id = kwargs['pk'])
  return render(request,'ImageApp/book_detail.html',{'book':book})    
  


class BookUpdateView(View):
  def get(self,request,pk,*args,**kwargs):
    book = Book.objects.get(pk = pk)
    form = BookCreateForm(instance=book,)
    return render(request,'ImageApp/book_update.html',{'form':form})
  def post(self,request,pk,*args,**kwargs):
    book = Book.objects.get(pk = pk)
    form = BookCreateForm(instance=book, data = request.POST,files = request.FILES)
    if form.is_valid():
      form.save()
      return redirect('book-detail', pk = book.pk)
    return book.get(request,pk)  

    
class BookDeleteView(View):
  def get(self,request,pk,*args,**kwargs):
    book = Book.objects.get(id = kwargs[pk])
    form = ConfirmForm()
    return render(request,'ImageApp/book_confirm_delete.html',{'form':form,'book':book})
  def post(self,request,*args,**kwargs):
    book = Book.objects.get(id = kwargs[pk])
    form = ConfirmForm(data = request.POST,files = request.FILES)
    if form.is_valid():
      form.Delete()
      return redirect('book-list')
    return book.get(request,id = kwargs[pk])

def UserProfile(request):
  form = UserForm(request.POST,request.FILES)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = UserForm()
  return render(request, 'ImageApp/user_info.html',{'form':form})       


from django.forms import formset_factory

def UserInfo(request):
  formset = formset_factory(form = UserForm,extra= 6)
  if request.method =='POST':
    form = formset(request.POST,request.FILES)
    if form.is_valid():
      for data in form:
        data.save() #save to database
      return redirect('home')

  return render(request,'ImageApp/user_formset.html',{'formset':formset})




def Display_info(request):
  name = ['ben','sara','etim','tom']
  age = 10

  return render(request,'ImageApp/display_info.html',{'name':name,'age':age})

from django.contrib.auth import authenticate,login
def SignUp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username = username,password = raw_password)
      login(request,user)
      return redirect('home')
  else:
   form = SignUpForm()
  return render(request, 'ImageApp/signup.html',{'form':form})


from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.urls import reverse_lazy

class Login(LoginView):
  form_class = LoginForm
  template_name = 'ImageApp/login.html'
  #success_url = reverse_lazy('home')

class Logout(LogoutView):
  template_name = 'ImageApp/logout.html'  


class PasswordReset(PasswordResetView):
  template_name = 'ImageApp/password_reset.html'
  success_url = reverse_lazy("password_reset_done")
  subject_template_name = "ImageApp/password_reset_subject.txt"
  email_template_name = "ImageApp/password_reset_email.html"


class PasswordResetDone(PasswordResetDoneView): 
  template_name = 'ImageApp/password_reset_done.html' 

class PasswordResetConfirm(PasswordResetConfirmView):
  template_name = 'ImageApp/password_reset_confirm.html'  
  success_url = reverse_lazy("password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
  template_name = 'ImageApp/password_reset_complete.html'  










