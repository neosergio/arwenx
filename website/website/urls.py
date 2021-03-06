from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','docswarehouse.views.inicio'),
	url(r'^ingresar/$','docswarehouse.views.ingresar'),
	url(r'^usuario/editar/password/$','docswarehouse.views.cambiar_password'),
	url(r'^salir/$','docswarehouse.views.salir'),
	url(r'^resoluciones/$','docswarehouse.views.resoluciones'),
	url(r'^resoluciones/nueva/$','docswarehouse.views.nueva_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/$','docswarehouse.views.detalle_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/editar$','docswarehouse.views.editar_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/borrar$','docswarehouse.views.borrar_resolucion'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/agregar/interesado/$','docswarehouse.views.nuevo_interesado'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/quitar/interesado/$','docswarehouse.views.quitar_interesado'),
	url(r'^resolucion/(?P<id_resolucion>\d+)/quitar/interesado/confirmar/(?P<id_interesado>\d+)/$','docswarehouse.views.confirmar_quitar_interesado'),
	url(r'^buscar/$','docswarehouse.views.buscar_resolucion'),
	url(r'^administrar/', include(admin.site.urls)),
	url(r'^interesados/$', 'docswarehouse.views.interesados'),
	url(r'^interesados/editar/(?P<id_interesado>\d+)/$', 'docswarehouse.views.editar_interesado'),
	url(r'^interesados/nuevo/$', 'docswarehouse.views.nuevo_interesado'),
	url(r'^categorias/$', 'docswarehouse.views.categorias'),
	url(r'^categorias/nueva$', 'docswarehouse.views.nueva_categoria'),
	url(r'^categorias/(?P<id_categoria>\d+)/editar$', 'docswarehouse.views.editar_categoria'),
	url(r'^facultades/$', 'docswarehouse.views.facultades'),
	url(r'^facultades/nueva$', 'docswarehouse.views.nueva_facultad'),
	url(r'^facultades/(?P<id_facultad>\d+)/editar$', 'docswarehouse.views.editar_facultad'),
)

handler404 = "docswarehouse.views.page404"
handler500 = "docswarehouse.views.page500"