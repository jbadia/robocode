from django.core.management.base import NoArgsCommand
from robocode.registration.models import UserProfile, User

class Command(NoArgsCommand):

    help = "This doesn't do anything yet"

    def handle(self, **options):
        print "\nllista d'equips amb els corresponents usuaris i facultats:"
        user_profile_list = UserProfile.objects.all()
        if len(user_profile_list)<1:
            print "   No hi han usuaris registrats"
        for profile in user_profile_list:
            print "  ", User.objects.get(id=profile.user.id).username, '/', profile.integrants, '/', profile.escola_universitat       
        print
