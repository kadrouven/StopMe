from django.db import models

class Stations(models.Model):
    stationName = models.CharField(max_length=128, unique=True)
    lat = models.CharField(max_length=128)
    lng = models.CharField(max_length=128)
	
    def __unicode__(self):
        return self.stationName