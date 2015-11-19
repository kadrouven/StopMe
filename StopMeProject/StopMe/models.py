from django.db import models

class Station(models.Model):
    stationName = models.CharField(max_length=128, unique=True, null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    lng = models.FloatField(null=False, blank=False)
    transtype = models.CharField(max_length=128)

    def __unicode__(self):
#        return self.stationName
        return str(self.id)

class Route(models.Model):
    serviceNumber = models.CharField(max_length = 10, null=True, blank=True)
    origin = models.CharField(max_length = 128, null=False, blank=False)
    destination = models.CharField(max_length = 128, null=False, blank=False)
    via = models.CharField(max_length = 128, null=True, blank=True)

    def __unicode__(self):
#       return self.origin + ' to ' + self.destination + ' via ' + self.via
        return str(self.id)

class RouteStations(models.Model):
    routeID = models.ForeignKey(Route)
    stationID = models.ForeignKey(Station)

    def __unicode__(self):
#       return "ID: " + str(self.id) + " Route: " + str(self.routeID) + " Station: " + str(self.stationID)
        return str(self.id)