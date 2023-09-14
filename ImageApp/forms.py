# from dataclasses import field, fields
# import email
# import profile
from django import forms
# import profile
from .models import *
from django.forms import ModelForm

class TeamForm(ModelForm):
 class Meta:
  model = Profile
  fields = '__all__'

class BookCreateForm(ModelForm):
 class Meta:
  model = Book
  fields = '__all__'  


class ConfirmForm(forms.Form):
  confirm = forms.BooleanField(label = 'confirm')

class UserForm(forms.Form):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  email = forms.EmailField()
  profile_image = forms.ImageField()
  '''
  from django.forms import ModelForm
  class UserForm(ModelForm):
    class Meta:
      model = UserInfo
      fields = '__all__'
      '''


from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['email'].widget.attrs['placeholder'] = 'Email'
    self.fields['username'].widget.attrs['placeholder'] = 'UserName'
    self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password1'].widget.attrs['placeholder'] = 'password'
  class Meta:
    model = User
    fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2') 

class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)

    self.fields['password'].widget.attrs['placeholder'] = 'Password'
    self.fields['username'].widget.attrs['placeholder'] = 'Username'
    