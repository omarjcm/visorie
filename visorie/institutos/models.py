#encoding:utf-8
from django.contrib.gis.db import models

class Institutos_Educativos(models.Model):
    ie_id = models.FloatField()
    ie_canton_cod = models.CharField(max_length=254)
    ie_canton = models.CharField(max_length=254)
    ie_parroquia = models.CharField(max_length=254)
    ie_codigo_distrito = models.CharField(max_length=254)
    ie_t_sede = models.CharField(max_length=254)
    ie_circuito_cod = models.CharField(max_length=254)
    ie_casos_exce = models.FloatField()
    ie_institucion = models.CharField(max_length=254)
    ie_ute = models.FloatField()
    ie_unidad_eje = models.CharField(max_length=254)
    ie_codigo_ue = models.CharField(max_length=254)
    ie_sin_nombre = models.CharField(max_length=254)
    ie_region = models.CharField(max_length=254)
    ie_sostenimiento = models.CharField(max_length=254)
    ie_regimen = models.CharField(max_length=254)
    ie_jurisdiccion = models.CharField(max_length=254)
    ie_tipo_educacion = models.CharField(max_length=254)
    ie_escolarizacion = models.CharField(max_length=254)
    ie_modalidad = models.CharField(max_length=254)
    ie_jornada = models.CharField(max_length=254)
    ie_genero_ofertado = models.CharField(max_length=254)
    ie_nivel_educacion = models.CharField(max_length=254)
    ie_administracion = models.CharField(max_length=254)
    ie_financiamiento = models.CharField(max_length=254)
    ie_zona_institucion = models.CharField(max_length=254)
    ie_zona_inec = models.CharField(max_length=254)
    ie_forma_gestion = models.CharField(max_length=254)
    ie_etnia = models.CharField(max_length=254)
    ie_nacionalidad = models.CharField(max_length=254)
    ie_pueblo = models.CharField(max_length=254)
    ie_docentes = models.FloatField()
    ie_administrativo = models.FloatField()
    ie_anio3 = models.FloatField()
    ie_anio4 = models.FloatField()
    ie_grado1 = models.FloatField()
    ie_grado2 = models.FloatField()
    ie_grado3 = models.FloatField()
    ie_grado4 = models.FloatField()
    ie_grado5 = models.FloatField()
    ie_grado6 = models.FloatField()
    ie_grado7 = models.FloatField()
    ie_grado8 = models.FloatField()
    ie_grado9 = models.FloatField()
    ie_grado10 = models.FloatField()
    ie_curso1 = models.FloatField()
    ie_curso2 = models.FloatField()
    ie_curso3 = models.FloatField()
    ie_alfabetiza = models.FloatField()
    ie_formacion = models.FloatField()
    ie_formacion1 = models.FloatField()
    ie_no_escolar = models.FloatField()
    ie_otros = models.FloatField()
    ie_total_estu = models.FloatField()
    ie_total_cons = models.FloatField()
    ie_estudiante = models.FloatField()
    ie_estudian_1 = models.FloatField()
    ie_tipo_especialidad = models.CharField(max_length=254)
    ie_especialidades = models.CharField(max_length=254)
    ie_discapacidad = models.CharField(max_length=254)
    ie_unidocente = models.CharField(max_length=254)
    ie_acceso = models.CharField(max_length=254)
    ie_tipo_de_calle = models.CharField(max_length=254)
    ie_energia_planta = models.CharField(max_length=254)
    ie_red_publica = models.CharField(max_length=254)
    ie_energia_solar = models.CharField(max_length=254)
    ie_internet = models.CharField(max_length=254)
    ie_biblioteca = models.CharField(max_length=254)
    ie_computadoras = models.FloatField()
    ie_terreno = models.FloatField()
    ie_construccion = models.FloatField()
    ie_aulam2 = models.FloatField()
    ie_num_pupitres = models.FloatField()
    ie_disenio = models.CharField(max_length=254)
    ie_cerramiento = models.CharField(max_length=254)
    ie_tenencia = models.CharField(max_length=254)
    ie_riesgo_primario = models.CharField(max_length=254)
    ie_riesgo_secundario = models.CharField(max_length=254)
    ie_inundacion = models.CharField(max_length=254)
    ie_beneficios = models.CharField(max_length=254)
    ie_comparte1 = models.CharField(max_length=254)
    ie_comparte2 = models.CharField(max_length=254)
    ie_comparte3 = models.CharField(max_length=254)
    ie_comparte4 = models.CharField(max_length=254)
    ie_laboratorios = models.CharField(max_length=254)
    ie_talleres = models.CharField(max_length=254)
    ie_x = models.FloatField()
    ie_y = models.FloatField()

    geom = models.MultiPointField(srid=32717)
    objects = models.GeoManager()

    def __str__(self):
        return self.ie_institucion


