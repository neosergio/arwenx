from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','docswarehouse.views.inicio'),
	url(r'^ingresar/$','docswarehouse.views.ingresar'),
	url(r'^salir/$','docswarehouse.views.salir'),
	url(r'^resoluciones/nueva/$','docswarehouse.views.nueva_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/$','docswarehouse.views.detalle_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/agregar/interesado/$','docswarehouse.views.nuevo_interesado'),
	url(r'^administrar/', include(admin.site.urls)),
	url(r'^instancia/nueva/$', 'docswarehouse.views.nueva_instancia'),
	url(r'^interesados/', 'docswarehouse.views.interesados'),
	url(r'^interesados/nuevo/$', 'docswarehouse.views.nuevo_interesado'),
)
