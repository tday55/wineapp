from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse

from .models import Wine

def index(request):
    latest_wine_list = Wine.objects.order_by('-acquisition_date')[:5]
    template = loader.get_template('winecat/index.html')
    context = RequestContext(request, {
        'latest_wine_list': latest_wine_list,
    })
    return HttpResponse(template.render(context))

def detail(request, wine_id):
    return HttpResponse("You're looking at wine %s." % wine_id)

def vineyard(request, wine_id):
    response = "You're looking at the vineyard of wine %s."
    return HttpResponse(response % wine_id)

def varietal(request, wine_id):
    return HttpResponse("You're seeing what varietal wine %s is." % wine_id)