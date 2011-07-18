from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext
from django.contrib.admin.views.decorators import staff_member_required
import os, sys
from django.contrib import auth
#from django.contrib.auth.views  import User
from robocode.uploader.models import *
#from robocode.uploader.models import Solver, User, Benchmark
from robocode.uploader.views import *
from robocode.registration.models import UserProfile
from robocode.schedule.views import comprovar_submit
from robocode.settings import *
import datetime

def index(request):
    """ Returns home space if user is authenticated and introduction page instead"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/introduccio/')

def login(request):
    """ Returns login site """
    return render_to_response('registration/login.html')


def logout(request):
    """ Logouts an logged user """
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


def user_profile(request, id_user):
    """ Returns user profile edition page """
    user = User.objects.get(id=id_user)
    integrants = UserProfile.objects.get(user=user).integrants
    escola_universitat = UserProfile.objects.get(user=user).escola_universitat
    if request.user != user:
        return render_to_response('invalid.html')
    return render_to_response('registration/edit_user.html', locals())


def edit_user(request, id_user, action):
    """ Edits user depending on method """
    if request.POST:
        #if there is a POST it means user changed something
        if action == 'profile':
            user = User.objects.filter(id=id_user).update(email = request.POST["email"])
            up = UserProfile.objects.filter(user=User.objects.get(id=id_user)).update(integrants = request.POST["integrants"], escola_universitat = request.POST["escola_universitat"])
            return HttpResponseRedirect("/edit/user/%s/" % id_user)
        elif action == 'passwd':
            u = User.objects.get(id=id_user)
            if u.check_password(request.POST["old_passwd"]):
                if request.POST["new_passwd"] == request.POST["confirm"]:
                    u.set_password(request.POST["new_passwd"])
                    u.save()
                else:
                    return HttpResponse("error2")
            else:
                #return HttpResponse("error1")
		pass_correcte = True
        	user = u 
        	#return render_to_response('registration/edit_user.html', locals())
		missatge = "Contrassenya actual incorrecta"
                return render_to_response('invalid.html', locals())
            return HttpResponseRedirect("/edit/user/%s/" % id_user)
        else:
            return HttpResponseRedirect("/invalid/")
    else:
        #if no POST then show user info
        user = User.objects.get(id=id_user)
        return render_to_response('registration/edit_user.html', {'user': user})


def menu(request, option):
        if request.user.is_authenticated():
            user = User.objects.get(username = request.user.username)
        return render_to_response('content/%s.html' % option, locals())

def media(request):
    return HttpResponseRedirect("media/")

def home(request):
    """Do authentication or show home page"""
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
        else:
            # Show an error page
            #return HttpResponseRedirect("/invalid/")
            return usuariInvalid(request)
    else:
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        else:
            user = User.objects.get(username = request.user.username)

    submits = Submit.objects.filter(user = User.objects.get(username=user.username))
    for submit in submits:
        submit.url='/site_media/submit/'+re.findall(settings.MEDIA_ROOT+'submit/(.*)',submit.file.name)[0]
    submit_obert = comprovar_submit()
    return render_to_response("main.html", locals())
     
def usuariInvalid(request):
    missatge = "Usuari, contrassenya incorrectes"
    return render_to_response('invalid.html', locals())

def invalid(request):
    return render_to_response('invalid.html')
    
def requirements(request):
    return render_to_response('requirements.html')

def str2bool(v):
    return v.lower() in ["yes", "true", "si", "s", "t", "1", 1]

@staff_member_required
def halt(self):
    os.system('halt')

@staff_member_required
def config(self, *args, **options):
    nomFitxer = '/home/mycode/robocode/settings.py'

    fitxer = open(nomFitxer,'r')
    temp=""
    for line in fitxer:
        if line[:len(args[0])] == args[0]:
            temp += args[0] + " = " + str(str2bool(args[1])) + "\n"
        else:
            temp += line
    fitxer.close()
    fitxer = open(nomFitxer,'w')
    fitxer.write(temp)
    os.system('sudo service httpd restart 2>/dev/null 1>/dev/null')
    return HttpResponseRedirect('/admin/')

