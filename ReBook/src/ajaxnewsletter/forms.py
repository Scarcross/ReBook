'''
Created on 16.07.2013

@author: leip
'''

from django import forms
class NewsletterForm(forms.Form):  
    email = forms.EmailField(label=_("E-mail address"))  