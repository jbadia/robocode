from django.core.management.base import BaseCommand
from robocode.registration.models import UserProfile, User
import os,sys

class Command(BaseCommand):

    help = "Reinici dels serveis"

    def handle(self, *args, **options):
	
	# S han de posar en l ordre de reinici
        serviceList = [ 'httpd' ]
        silent = '2>/dev/null 1>/dev/null'
        for argument in sys.argv[2:]:
	    if argument == 'nosilent':
                silent = ''

	for service in serviceList:
	    os.system('sudo service ' + service + ' stop ' + silent)
        serviceList.reverse()
	for service in serviceList:
            os.system('sudo service ' + service + ' start ' + silent)
