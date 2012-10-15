#encoding:utf-8
import os
import sys
import csv

PROJ_PATH = os.path.dirname(os.path.realpath(__file__))
DIR_PATH = os.path.abspath(os.path.join(PROJ_PATH, "website"))
csv_datos = os.path.join(PROJ_PATH, 'db/secretaria.csv')

sys.path.append(DIR_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from docswarehouse.models import Instancia
print "Empezando la migracion"

lector_registros = csv.reader(open(csv_datos), delimiter=',', quotechar = '\'')
for elemento in lector_registros:
	if elemento[0].startswith('0'):
		print elemento[0] + elemento[1]