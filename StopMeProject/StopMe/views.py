from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from StopMe.models import Station, Route, RouteStation

#def index(request):
#    return HttpResponse("Rango says hello world!")

def index(request):
    context = RequestContext(request)
    context_dict = {}
    station = Station.objects.filter(lat__range=(55.868030,55.870230), type="Train")
    context_dict["station"] = station
    route = Route.objects.all()
    context_dict["route"] = route
    routestations = RouteStation.objects.all()
    context_dict["routestations"] = routestations
    return render_to_response('StopMe/index.html', context_dict, context)

def chooseTransport(request):
    context = RequestContext(request)
    context_dict = {}
    station = Station.objects.all()
    context_dict["station"] = station
    route = Route.objects.all()
    context_dict["route"] = route
    routestations = RouteStation.objects.all()
    context_dict["routestations"] = routestations
    return render_to_response('StopMe/chooseTransport.html', context_dict, context)