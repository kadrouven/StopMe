from django.db import models

class Station(models.Model):
    stationName = models.CharField(max_length=128, unique=True)
    lat = models.CharField(max_length=128)
    lng = models.CharField(max_length=128)

    def __unicode__(self):
        return self.stationName

class Route(models.Model):

    origin = models.CharField(max_length = 128)
    destination = models.CharField(max_length = 128)
    via = models.CharField(max_length = 128)

    def __unicode__(self):
    	return origin+' to '+destination+' via '+via #could change this string output


class RouteStations(models.Model):
    routeID = models.ForeignKey(Route)
    stationID = models.ForeignKey(Station)

    def __unicode__(self):
    	return routeID+stationID #could change this string output