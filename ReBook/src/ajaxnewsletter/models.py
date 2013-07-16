from django.db import models

# Create your models here.
class NewsletterEmails(models.Model):  
    email = models.EmailField((u"E-mail address"),)  