from django.conf.urls.defaults import *
from django.contrib import admin
from robocode.views import *
from robocode.schedule.views import *
from robocode.news.views import listNews
from robocode.registration.admin_views import reportUser


#from robocode.tempViewProva import exemple_img

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^variables/$', variables),
    (r'^halt/$', halt),
    (r'^config/([a-zA-Z_]*)/(True|False)', config),
    (r'^dates/$', listNews),
    (r'^$', index),
    (r'^login/', login),
    (r'^logout/', logout),
    (r'^home/', home),
    (r'^edit/user/(\d{1,2})/([a-z]*)/', edit_user),
    (r'^edit/user/(\d{1,2})/', user_profile),
    (r'^invalid/', invalid),
    (r'^upload/',include('robocode.uploader.urls')),
    (r'^signup/', include('robocode.registration.urls')),
    (r'^admin/userstatus/reports/$', reportUser),
    #(r'([a-z]*/)', menu), # no se que pinta aquest
    # Example:
    # (r'^robocode/', include('robocode.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
#url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$', 'chronograph.views.job_run', name="admin_chronograph_job_run")

