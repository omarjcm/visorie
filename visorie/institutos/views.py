#encoding:utf-8
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.core import serializers
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D

from institutos.models import Institutos_Educativos

# Create your views here.

def index(request):
	data = {}
	pnt = Polygon(((-79.9409447, -2.1931734), (-79.9284134, -2.1652986), (-79.9199591,-2.2070678), (-79.9294434, -2.2270942), (-79.9409447, -2.1931734)))
	data['institutos'] = Institutos_Educativos.objects.all()
	data['institutos_within'] = Institutos_Educativos.objects.filter(geom__within=pnt)
	data['institutos_left'] = Institutos_Educativos.objects.filter(geom__left=pnt)
	data['institutos_right'] = Institutos_Educativos.objects.filter(geom__right=pnt)
#	data['institutos'] = Institutos_Educativos.objects.all()
	return render_to_response("base.html", data)
