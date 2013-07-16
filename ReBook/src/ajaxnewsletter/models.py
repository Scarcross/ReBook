from django.db import models

# Create your models here.
class NewsletterEmails(models.Model):  
    email = models.EmailField(_(u"E-mail address"),)  