from django.contrib.gis import admin
from .models import Institutos_Educativos

admin.site.register(Institutos_Educativos, admin.OSMGeoAdmin)
