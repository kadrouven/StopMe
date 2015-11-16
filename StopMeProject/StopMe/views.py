from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from StopMe.models import Stations

#def index(request):
#    return HttpResponse("Rango says hello world!")

def index(request):
    context = RequestContext(request)
    context_dict = {}
    station = Stations.objects.get(stationName="Partick")
    context_dict['station'] = station
    return render_to_response('StopMe/index.html', context_dict, context)