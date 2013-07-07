from django.db import models

# Create your models here.
class Book(models.Model):
    bookname = models.CharField(max_length=300)
    condition = models.CharField(max_length= 300)
    
class LastOwner(models.Model):
    book = models.ForeignKey(Book)
    email = models.EmailField()
    