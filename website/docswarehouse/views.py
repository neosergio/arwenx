from docswarehouse.models import Instancia, Resolucion, Interesado
from docswarehouse.forms import InstanciaForm, ResolucionForm, InteresadoForm, BuscarForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

login_url_variable = '/ingresar'

@login_required(login_url=login_url_variable)
def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('no_activo.html')
			else:
				return render_to_response('no_usuario.html')
	else:
		form = AuthenticationForm(auto_id=True)
	return render_to_response('ingresar.html',{'form':form}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url=login_url_variable)
def nueva_resolucion(request):
	if request.method == 'POST':
		formulario = ResolucionForm(request.POST)
		if formulario.is_valid():
			resolucion_previo = formulario.save(commit=False)
			resolucion_previo.registro = request.user
			resolucion_previo.save()
			redireccion = "/resolucion/%i" % (resolucion_previo.id)
			return HttpResponseRedirect(redireccion)
	else:
		formulario = ResolucionForm()
	return render_to_response('nueva_resolucion.html',{'form':formulario}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def detalle_resolucion(request, id_resolucion):
	resolucion = get_object_or_404(Resolucion, pk=id_resolucion)
	return render_to_response('detalle_resolucion.html', {'resolucion':resolucion}, context_instance=RequestContext(request))


@login_required(login_url=login_url_variable)
def nuevo_interesado(request, id_resolucion):
	if request.method == 'POST':
		formulario = InteresadoForm(request.POST)
		resolucion = Resolucion.objects.get(pk=id_resolucion)
		if formulario.is_valid():
			nombre_interesado = formulario.cleaned_data['nombre']
			try:
				interesado = Interesado.objects.get(nombre__exact=nombre_interesado)
			except:
				interesado = Interesado.objects.create(nombre=nombre_interesado, registro=request.user)
			resolucion.interesado.add(interesado)
			redireccion = '/resolucion/'+id_resolucion
			return HttpResponseRedirect(redireccion)
	else:
		formulario = InteresadoForm()
	return render_to_response('nuevo_interesado.html',{'form':formulario},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def quitar_interesado(request, id_resolucion):
	resolucion = get_object_or_404(Resolucion, pk=id_resolucion)
	return render_to_response('quitar_interesado.html',{'resolucion':resolucion}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def confirmar_quitar_interesado(request, id_resolucion, id_interesado):
	resolucion = get_object_or_404(Resolucion, pk=id_resolucion)
	interesado = get_object_or_404(Interesado, pk=id_interesado)
	resolucion.interesado.remove(interesado)
	redireccion = '/resolucion/' + str(id_resolucion) + '/quitar/interesado'
	return HttpResponseRedirect(redireccion)

@login_required(login_url=login_url_variable)
def resoluciones(request):
	datos = Resolucion.objects.all()
	return render_to_response('resoluciones.html',{'datos':datos},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def buscar_resolucion(request):
	form = BuscarForm()
	return render_to_response('buscar.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def nueva_instancia(request):
	if request.method == 'POST':
		formulario = InstanciaForm(request.POST)
		if formulario.is_valid():
			instancia_previo = formulario.save(commit=False)
			instancia_previo.registro = request.user
			instancia_previo.save()
			return HttpResponseRedirect('/')
	else:
		formulario = InstanciaForm()
	return render_to_response('nueva_instancia.html',{'form':formulario},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def interesados(request):
	datos = Interesado.objects.all()
	return render_to_response('interesados.html',{'datos':datos},context_instance=RequestContext(request))
