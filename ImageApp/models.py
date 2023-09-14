# import email
# from tabnanny import verbose
# from unicodedata import category
# from distutils.command.upload import upload
# from email.mime import image
# from tabnanny import verbose
# from venv import create
from django.db import models
import datetime



# Create your models here.


class Categories(models.Model):
 title = models.CharField(max_length=100)

 def __str__(self):
  return f'{self.title}'

 class Meta:
  verbose_name_plural = 'Categories'

class Profile(models.Model):
 category = models.ForeignKey(Categories,on_delete=models.CASCADE)
 email = models.EmailField()
 name = models.CharField(max_length=100)
 image = models.FileField(upload_to='Files/',default='')
 description = models.TextField()

 def __str__(self):
  return f'{self.name}' 
 class meta:
  ordering = ['-name']

class Book(models.Model):
  title = models.CharField(max_length=100)
  image = models.FileField(upload_to='books/')
  description = models.TextField()
  author = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
  discount = models.CharField(max_length=100)
  isbn = models.CharField(max_length=100,unique=True)
  is_published = models.BooleanField(default=True)
  ratings = models.IntegerField()
  create_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-create_date']

  def __str__(self):
    return self.title

class UserInfo(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  profile_image = models.ImageField(upload_to = 'Profile_Image')
  def __str__(self):
    return f'{self.first_name} {self.last_name}'
  class Meta:
    verbose_name_plural = 'UserInfo'  





  
