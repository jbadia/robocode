#!/bin/python

import os
import re
import time
import sys
import socket
from threading import Thread
import smtplib
from email.mime.text import MIMEText
import sys, os, re, urllib2, datetime, random
from time import sleep

# Preamble so we can use Django's DB API                                                                                                   
sys.path.append('/home/mycode/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'robocode.settings'

# Load up Django                                                                                                                           
from django.db import models
from robocode.registration.models import UnregisteredUser


PING_POLLING_TIME = 60*60

def email_notification(topic, msg):
    FROMADDR = "maxsat@diei.udl.cat"
    LOGIN    = "maxsat"
    PASSWORD = "mS4tvlt0"
    SUBJECT  = "[Supervisor: %s][%s]" % (topic,time.strftime("%d %b %Y %H:%M:%S ", time.localtime()))
    ADMIN_MAILS = "jbadia9@alumnes.udl.cat, maxsat@diei.udl.cat"

    miss = MIMEText(msg)
    miss['Subject'] = SUBJECT
    miss['To'] = ADMIN_MAILS

    server = smtplib.SMTP('smtps.udl.cat', 465)
    #server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)
    server.sendmail(FROMADDR, ADMIN_MAILS, miss.as_string())
    server.quit()

class db_status(Thread):
    def __init__(self, seconds):
        self.runTime = seconds
        Thread.__init__(self)
    def run(self):
        print "Started!"
        time.sleep(self.runTime)
        
        print "Checking Database"
        unregusers = UnregisteredUser.objects.all()

        if len(unregusers)>0:
            print "Unregistered user found"
            status_report = "There are %i unregisterd users in the database" % len(unregusers)
            email_notification("Unregistered Users Status", status_report)

            print "Going to sleep"
        t_aux = db_status(self.runTime)
        t_aux.start()
        #print time.ctime()

t = db_status(PING_POLLING_TIME)
t.start()
