from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from StopMe.models import Station, Route, RouteStations

#def index(request):
#    return HttpResponse("Rango says hello world!")

def index(request):
    context = RequestContext(request)
    context_dict = {}
    station = Station.objects.all()
    context_dict["station"] = station
    route = Route.objects.all()
    context_dict["route"] = route
    routestations = RouteStations.objects.all()
    context_dict["routestations"] = routestations
    return render_to_response('StopMe/index.html', context_dict, context)