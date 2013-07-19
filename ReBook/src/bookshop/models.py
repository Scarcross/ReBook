from django.db import models

# Create your models here.

#Entspricht dem Verlag  
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name

#Author des Buches
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length= 40)
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    
class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    isbn_13 = models.CharField(max_length=13)
    isbn_10 = models.CharField(max_length=10)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    
