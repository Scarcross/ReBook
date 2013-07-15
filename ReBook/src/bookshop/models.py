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
       
    
    def get_title(self):
        return self.__title


    def get_author(self):
        return self.__author


    def get_isbn(self):
        return self.__isbn


    def get_description(self):
        return self.__description


    def get_date(self):
        return self.__date


    def set_title(self, value):
        self.__title = value


    def set_author(self, value):
        self.__author = value


    def set_isbn(self, value):
        self.__isbn = value


    def set_description(self, value):
        self.__description = value


    def set_date(self, value):
        self.__date = value


    def del_title(self):
        del self.__title


    def del_author(self):
        del self.__author


    def del_isbn(self):
        del self.__isbn


    def del_description(self):
        del self.__description


    def del_date(self):
        del self.__date
