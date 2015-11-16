from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

#def index(request):
#    return HttpResponse("Rango says hello world!")

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('StopMe/index.html', context_dict, context)