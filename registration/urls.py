from django.conf.urls.defaults import *
from robocode.registration.views import *

urlpatterns = patterns('',
                       (r'^new/$',new),
                       (r'', signup),
                       
)
