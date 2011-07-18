from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from robocode.news.models import Event
#from django.contrib.auth.models import User

def listNews(request):
    news = Event.objects.all()
    #return render_to_response('news.html',{'news':news})
    return render_to_response('news.html', locals())
