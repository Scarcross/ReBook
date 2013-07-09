from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.title
    
    
