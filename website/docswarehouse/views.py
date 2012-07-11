from docswarehouse.models import Instancia
from docswarehouse.forms import InstanciaForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def nueva_instancia(request):
	formulario = InstanciaForm()
	if request.method == 'POST':
		instancia = InstanciaForm(request.POST)
		if instancia.is_valid():
			instancia_previo = instancia.save(commit=False)
			instancia_previo.registro = request.user
			instancia_previo.save()
	return render_to_response('nueva_instancia.html',{'form':formulario},context_instance=RequestContext(request))
