from robocode.registration.models import UserProfile, User
from robocode.uploader.views import *
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

## Mostrem els equips i els robots presentats
@staff_member_required
def reportUser(request):
    user_profile_list = []
    for perfil in UserProfile.objects.all():
        perfil.username = User.objects.get(id=perfil.user_id).username
        user_profile_list.append(perfil)

    submit_list = []
    for sub in Submit.objects.all():
        sub.categoria = Category.objects.get(id=sub.category_id).name
        sub.filename = unicode(unicode(sub.file).rsplit('/',1)[1])
        submit_list.append(sub)

    return render_to_response('admin/report.html' ,{'user_profile_list': user_profile_list, 'submit_list': submit_list})
