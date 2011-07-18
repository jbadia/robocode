from django.conf.urls.defaults import *
from robocode.uploader.views import *

urlpatterns = patterns('',
                       (r'([a-z]*)/([a-z]*)/(\d{1,2})/$', actions),
                       (r'add/([a-z]*)/$', add_model),
                       
)
