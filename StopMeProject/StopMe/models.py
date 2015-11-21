from django.db import models

class Station(models.Model):
    stationName = models.CharField(max_length=128, unique=True, null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    lng = models.FloatField(null=False, blank=False)
    type = models.CharField(max_length=128)

    def __unicode__(self):
        return str(self.stationName)

class Route(models.Model):
    serviceNumber = models.CharField(max_length = 10, null=True, blank=True)
    origin = models.CharField(max_length = 128, null=False, blank=False)
    destination = models.CharField(max_length = 128, null=False, blank=False)
    via = models.CharField(max_length = 128, null=True, blank=True)

    def __unicode__(self):
      return self.destination

class RouteStation(models.Model):
    route = models.ForeignKey(Route)
    station = models.ForeignKey(Station)

    def __unicode__(self):
      return str(self.route) + " " + str(self.station)