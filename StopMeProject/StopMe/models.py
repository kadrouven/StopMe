from django.db import models

class Station(models.Model):
    stationName = models.CharField(max_length=128, unique=True)
    lat = models.CharField(max_length=128)
    lng = models.CharField(max_length=128)

    def __unicode__(self):
#        return self.stationName
		return str(self.id)

class Route(models.Model):

    origin = models.CharField(max_length = 128)
    destination = models.CharField(max_length = 128)
    via = models.CharField(max_length = 128)

    def __unicode__(self):
#    	return self.origin + ' to ' + self.destination + ' via ' + self.via
		return str(self.id)

class RouteStations(models.Model):
    routeID = models.ForeignKey(Route)
    stationID = models.ForeignKey(Station)

    def __unicode__(self):
#    	return "ID: " + str(self.id) + " Route: " + str(self.routeID) + " Station: " + str(self.stationID)
		return str(self.id)