from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from StopMe.models import Station, Route, RouteStation

def index(request):
    context = RequestContext(request)
    context_dict = {}
    station = Station.objects.filter(lat__range=(55.868030,55.870230), type=" Train")
    context_dict["station"] = station
    route = Route.objects.all()
    context_dict["route"] = route
    routestations = RouteStation.objects.all()
    context_dict["routestations"] = routestations
    return render_to_response('StopMe/index.html', context_dict, context)

def search(request):
    context = RequestContext(request)
    context_dict = {}
    
    type = Station.objects.values("type").distinct()
    context_dict["type"] = type
    
    if request.POST.get("type", ""):
        context_dict["selected_type"] = request.POST.get("type", "")
        origin = Station.objects.filter(type=(request.POST.get("type", "")))
        context["origin"] = origin
        print "------", request.POST.get("type", "")
        
    if request.POST.get("origin", ""):
        context_dict["selected_origin"] = request.POST.get("origin", "")
        route = RouteStation.objects.filter(station__stationName=request.POST.get("origin", ""))
        context_dict["route"] = route
    
    if request.POST.get("route", ""):
        context_dict["selected_route"] = request.POST.get("route", "")
        destination = RouteStation.objects.filter(route__destination__stationName=request.POST.get("route", ""))
        context_dict["destination"] = destination

    return render_to_response('StopMe/search.html', context_dict, context)

def map(request):
    context = RequestContext(request)
    context_dict = {}
    context_dict["final_destination"] = Station.objects.get(stationName=request.POST.get("destination", ""))
    return render_to_response('StopMe/map.html', context_dict, context)
    