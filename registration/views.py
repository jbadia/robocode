# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from robocode.registration.forms import SignupForm
from robocode.registration.models import *
from robocode.uploader.models import UserProfile
from robocode.registration.admin import confirm_registration_user, correu_confirmacio
from robocode.settings import *
from robocode.schedule.views import comprovar_registre
import smtplib
from email.mime.text import MIMEText


def signup(request):
    """ Build signup form """
    form = UnregisteredUserForm()
    usuari_existent = False
    registre_obert = comprovar_registre()
    return render_to_response('registration/signup.html', locals())
    
def new(request):
    """ Save registration """
    try:
        usuari_existent = False
        form = UnregisteredUserForm(request.POST)
        newuser = form.save()
        registre_obert = comprovar_registre()
        ## registrem l'usuari sense validacio manual
        confirm_registration_user(newuser)
        #correu_confirmacio(newuser)
        return render_to_response('registration/signed.html', locals())
    except ValueError:
        return render_to_response('registration/signup.html', locals())
    except:
        usuari_existent = True
        return render_to_response('registration/signup.html', locals())


def email_notification(user):
    FROMADDR = "maxsat@diei.udl.cat"
    LOGIN    = "maxsat"
    PASSWORD = "mS4tvlt0"
    SUBJECT  = "Registre Robocode"
    DEST_MAILS = user.email
    msg = u"\nBenvolgut %s,\nGràcies per registrar-se a Robocode.\n Tot seguit se li enviarà un correu confirmant el seu login i password.\nSalutacions cordials.\n\n---\nOrgantizació del Robocode\n" % user.first_name

    miss = MIMEText(msg)
    miss['Subject'] = SUBJECT
    miss['To'] = DEST_MAILS

    server = smtplib.SMTP('smtps.udl.cat', 465)
    #server.set_debuglevel(1)                                                                                                              
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, DEST_MAILS, miss.as_string())
    server.sendmail(FROMADDR, "maxsat@diei.udl.cat", miss.as_string())
    server.quit()

