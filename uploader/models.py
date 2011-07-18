# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ModelForm
from django import forms
from robocode.registration.models import UserProfile

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Submit(models.Model):
    title = models.CharField(max_length=50, verbose_name='Títol')
    user = models.ForeignKey(User) 
    category = models.ForeignKey(Category, verbose_name='Categoria')
    #category = models.ManyToManyField(Category)
    file = models.FileField(upload_to='%ssubmit/' % settings.MEDIA_ROOT, verbose_name='Fitxer')
    comments = models.TextField(verbose_name='Descripció')
    
    def __unicode__(self):
        return "%s" % self.title
    
    def tipus(self):
        return 'submit'
    

class SubmitForm(ModelForm):

    class Meta:
        model = Submit  
        exclude = ('user',)
        fields = ('title', 'file', 'category', 'comments',)

