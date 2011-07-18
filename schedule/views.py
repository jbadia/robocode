from robocode.schedule.models import *
from django.shortcuts import render_to_response
import datetime

def comprovar_event(event):
    ara = datetime.datetime.now()
    for element in ScheduledEvents.objects.filter(tipus_event=event):
        #if element.data_inici.__le__(ara) and element.data_final.__ge__(ara):
        if element.data_inici <= ara and element.data_final >= ara:
            return True
    return False

def comprovar_registre():
    return comprovar_event("REGISTRE_OBERT")

def comprovar_submit():
    return comprovar_event("SUBMIT_OBERT")

def variables(request):
    registre = comprovar_registre()
    submit = comprovar_submit()
    return render_to_response('variables.html',{'registre':registre, 'submit':submit})
