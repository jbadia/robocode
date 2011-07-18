from django.db import models
from django.contrib import admin

class Event(models.Model):
    event = models.CharField(max_length=350)
    data = models.DateTimeField()
    
    def __unicode__(self):
        return self.event
    
    class Meta:
        ordering = ["data"]
        
class EventAdmin(admin.ModelAdmin):
    list_display=('event','data')
    
admin.site.register(Event, EventAdmin)
