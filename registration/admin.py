#-*- coding: utf-8 -*-

from django.contrib import admin
from robocode.registration.models import UnregisteredUser
import smtplib
from email.mime.text import MIMEText
from django.contrib import auth
from django.contrib.auth.models import User
from robocode.registration.models import UserProfile

## S'han conservat aquestes variables per arreglar el problema de correu de la Robocode (referència MaxSAT)
FROMADDR = "maxsat@diei.udl.cat"
LOGIN    = "maxsat"
PASSWORD = "mS4tvlt0"
SUBJECT  = "Registre Robocode"

## Métode de registre de la MaxSAT (enviament correu)
def confirm_registration(self, request, queryset):
    msg = "\nDear %s,\n\nYour registration to the MaxSAT Evaluation has been confirmed by our administrator. You can login with your profile.\n\nHere you have a summary of your profile:\n+ Username:%s\n+ Password:%s\n\nMaxSAT Evaluation organizers"

    server = smtplib.SMTP('smtps.udl.cat', 465)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    for user in queryset:
        msg = msg % (user, user.username, user.password)
        miss = MIMEText(msg)
        miss['Subject'] = SUBJECT
        miss['To'] = user.email

        server.sendmail(FROMADDR, user.email , miss.as_string())
        u = User(first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email)
        u.set_password(user.password)
        u.save()
        up = UserProfile(user_id=u.id, organization=user.organization)
        up.save()
        user.delete()
    server.quit()

confirm_registration.short_description = "Confirm registration"

def confirm_registration_user(user):
    u = User(first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email)
    
    u.set_password(user.password)
    u.save()
    up = UserProfile(user_id=u.id, integrants=user.integrants, escola_universitat=user.escola_universitat)
    up.save()
    user.delete()
    #correu_confirmacio(u)

## TODO Corretgir problema sendmail
def correu_confirmacio(user):
    msg = "\nBenvolgut %s,\n\nEl registre al Robocode s'ha efectuat correctament. Pot accedir amb el seu perfil.\n\nAquí té un resum del seu perfil:\n+ Username:%s\n+ Password:%s\n\nOrganització Robocode"
    server = smtplib.SMTP('smtps.udl.cat', 465)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    msg = msg % (user, user.username, user.password)
    miss = MIMEText(msg)
    miss['Subject'] = SUBJECT
    miss['To'] = user.email
    server.sendmail(FROMADDR, user.email , miss.as_string())

class UnregisteredUserAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ['escola_universitat', 'integrants']
    actions = [confirm_registration]


admin.site.register(UnregisteredUser, UnregisteredUserAdmin)
admin.site.register(UserProfile)
