from django.db import models
from django.contrib import admin


class ScheduledEvents(models.Model):
    TIPUS_EVENT=(
        ('REGISTRE_OBERT','REGISTRE'),
        ('SUBMIT_OBERT','SUBMIT'),
    )
    nom_event = models.CharField(max_length=30)
    data_inici = models.DateTimeField()
    data_final = models.DateTimeField()
    tipus_event = models.CharField(max_length=20, choices=TIPUS_EVENT)

    def __unicode__(self):
        return self.nom_event

    class Meta:
        ordering = ["data_inici"]

class ScheduledEventsAdmin(admin.ModelAdmin):
    verbose_name = "Events programats"
    list_display = ('nom_event','data_inici','data_final','tipus_event')

admin.site.register(ScheduledEvents, ScheduledEventsAdmin)
