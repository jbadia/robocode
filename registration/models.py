from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UnregisteredUser(models.Model):
    username = models.CharField(max_length=30, verbose_name='Equip')
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    integrants = models.CharField(max_length=300)
    escola_universitat = models.CharField(max_length=30)
    confirm = models.BooleanField()

    def __unicode__(self):
        return '%s' % (self.username)


class UnregisteredUserForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
  
    class Meta:
        model = UnregisteredUser
        exclude = ('confirm','first_name','last_name',)
        fields = ('username','password', 'confirm_password', 'email','integrants','escola_universitat',)



#
# Extending User class according to http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/
#

class UserProfile(models.Model):
    integrants = models.CharField(max_length=300)
    escola_universitat = models.CharField(max_length=30)
    user = models.ForeignKey(User, unique=True, related_name='usuari') 
    def __unicode__(self):
        return '%s' % (self.user.username)
