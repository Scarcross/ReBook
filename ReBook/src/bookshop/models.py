# -*- coding: utf-8 -*-
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

# Genre things
class Genre(models.Model):
    
    NAME_CHOICES = (
        ('ER','Erotik'),
        ('AB','Abenteuer'),
        ('OC','Andere Länder'),
        ('DO','Arzt'),
        ('SD','Besondere Schicksale'),
        ('SJ','Besonders für Jugendliche'),
        ('SE','Bewährte Unterhaltung'),
        ('BI','Biographie'),
        ('CC','Comic'),
        ('CO','Computer'),
        ('ER','Erotik'),
        ('EZ','Erzählungen'),
        ('ET','Essen und Trinken'),
        ('FE','Familie'),
        ('FA','Fantasy'),
        ('FI','Film / Filmbuch'),
        ('FL','Fremdsprachige Literatur'),
        ('W','Frauen'),
        ('FP','Für Eltern'),
        ('GM','Gerichtsmedizin'),
        ('HS','Geschichte'),
        ('HO','Grusel'),
        ('FU','Heiteres'),
        ('HT','Historisches'),
        ('HB','Hobby'),
        ('IN','Indianer'),
        ('KB','Kinderbücher'),
        ('KL','Klassiker'),
        ('WA','Krieg'),
        ('KR','Krimi'),
        ('KU','Kunst'),
        ('LO','Liebe'),
        ('LY','Lyrik'),
        ('MA','Märchen'),
        ('NT','Natur und Tiere'),
        ('PY','Psychologie'),
        ('TR','Reisen'),
        ('RE','Religion'),
        ('SF','Science fiction'),
        ('SP','Sport'),
        ('T','Technik'),
        ('TH','Thriller'),
        ('KN','Wissen'),
        ('HU','Witz / Satire'),
)
    
    
    genrename = models.CharField(max_length=2,choices=NAME_CHOICES)
    def __unicode__(self):
        return u'%s'%(self.genrename)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    genre = models.ForeignKey(Genre)
    isbn_13 = models.CharField(max_length=13)
    isbn_10 = models.CharField(max_length=10)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
    class Meta:
        get_latest_by = 'date_added'
