#encoding:utf-8
import os
import sys
import csv

PROJ_PATH = os.path.dirname(os.path.realpath(__file__))
DIR_PATH = os.path.abspath(os.path.join(PROJ_PATH, "website"))
csv_datos = os.path.join(PROJ_PATH, 'db/secretaria.csv')

sys.path.append(DIR_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from docswarehouse.models import Resolucion
from docswarehouse.models import Instancia, Categoria
from docswarehouse.models import Facultad, Interesado
from django.contrib.auth.models import User
print "Empezando la migracion"

lector_registros = csv.reader(open(csv_datos), delimiter=';', quotechar = '`')
usuario = User.objects.get(pk=1)
contador = 0
for elemento in lector_registros:
    if elemento[0].startswith('0'):
        codigo_migrar = elemento[0]
        fecha_migrar = elemento[1]
        asunto_migrar = elemento[2]
        interesado_migrar, ok = Interesado.objects.get_or_create(nombre=elemento[3], registro=usuario)
        instancia_migrar, ok = Instancia.objects.get_or_create(nombre=elemento[4], registro=usuario)
        categoria_migrar, ok = Categoria.objects.get_or_create(nombre=elemento[5], registro=usuario)
        facultad_migrar, ok = Facultad.objects.get_or_create(nombre=elemento[6], registro=usuario)
        contador += 1
        print contador
        resolucion_ok, ok = Resolucion.objects.get_or_create(codigo_resolucion = codigo_migrar, fecha_emision = fecha_migrar,
            asunto = asunto_migrar, instancia = instancia_migrar, categoria = categoria_migrar,
            facultad = facultad_migrar, registro = usuario)
        resolucion_ok.interesado.add(interesado_migrar)
