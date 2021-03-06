# -*- coding: utf8 -*-
from docswarehouse.models import Instancia, Resolucion, Interesado, Categoria, Facultad
from docswarehouse.forms import InstanciaForm, ResolucionForm, InteresadoForm, BuscarForm, EditarInteresadoForm, CategoriaForm, FacultadForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
                    return render_to_response('no_activo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('no_usuario.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm(auto_id=True)
    return render_to_response('ingresar.html',{'form':form}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, auto_id=True, data=request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('confirmado.html', context_instance=RequestContext(request))
    else:
        form = PasswordChangeForm(request.user, auto_id=True)
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
    datos = Interesado.objects.all()
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
    return render_to_response('nuevo_interesado.html',{'form':formulario, 'interesados':datos, 'id':id_resolucion},context_instance=RequestContext(request))

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
    paginator = Paginator(datos, 500)
    page = request.GET.get('page')
    try:
        resoluciones = paginator.page(page)
    except PageNotAnInteger:
        resoluciones = paginator.page(1)
    except EmptyPage:
        resoluciones = paginator.page(paginator.num_pages)
    return render_to_response('resoluciones.html',{'resoluciones':resoluciones},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def editar_resolucion(request, id_resolucion):
    dato = get_object_or_404(Resolucion, pk=id_resolucion)
    if request.method == 'POST':
        formulario = ResolucionForm(request.POST, instance=dato)
        if formulario.is_valid():
            resolucion_previo = formulario.save(commit=False)
            resolucion_previo.registro = request.user
            resolucion_previo.save()
            redireccion = "/resolucion/%i" % (resolucion_previo.id)
            return HttpResponseRedirect(redireccion)
    else:
        formulario = ResolucionForm(instance=dato)
    return render_to_response('editar_resolucion.html',{'form':formulario, 'id':dato.pk}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def borrar_resolucion(request, id_resolucion):
    dato = get_object_or_404(Resolucion, pk=id_resolucion)
    dato.delete()
    return HttpResponseRedirect('/buscar')

@login_required(login_url=login_url_variable)
def buscar_resolucion(request):
    instancias = Instancia.objects.all()
    categorias = Categoria.objects.all()
    facultades = Facultad.objects.all()
    interesados = Interesado.objects.all()
    form = BuscarForm()
    resoluciones_resultantes = ''
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            codigo_consulta = ~Q(codigo_resolucion = '')
            fecha_consulta = ~Q(fecha_emision__isnull = True) | ~Q(fecha_emision__isnull = False)
            asunto_consulta = ~Q(asunto = '') | Q(asunto = '')
            instancia_consulta = ~Q(instancia__isnull = True)
            categoria_consulta = ~Q(categoria__isnull = True)
            facultad_consulta = ~Q(facultad__isnull = True) | ~Q(facultad__isnull = False)
            interesado_consulta = ~Q(interesado__isnull = True) | ~Q(interesado__isnull = False) 
            for k,v in request.POST.items():
                if k == 'codigo':
                    if v != '':
                        codigo_consulta = Q(codigo_resolucion = form.cleaned_data['codigo'])
                if k == 'fecha':
                    if v != '':
                        fecha_consulta = Q(fecha_emision = form.cleaned_data['fecha'])
                if k == 'asunto':
                    if v != '':
                        asunto_consulta = Q(asunto__icontains = form.cleaned_data['asunto'])
                if k == 'instancia':
                    if v != '':
                        instancia_consulta = Q(instancia = get_object_or_404(Instancia, nombre__iexact = form.cleaned_data['instancia']))
                if k == 'categoria':
                    if v != '':
                        categoria_consulta = Q(categoria = get_object_or_404(Categoria, nombre__iexact = form.cleaned_data['categoria']))
                if k == 'facultad':
                    if v != '':
                        facultad_consulta = Q(facultad = get_object_or_404(Facultad, nombre__iexact = form.cleaned_data['facultad']))
                if k == 'interesado':
                    if v != '':
                        interesado_consulta = Q(interesado__nombre__icontains = form.cleaned_data['interesado'])
            resoluciones_resultantes = Resolucion.objects.filter(codigo_consulta, fecha_consulta, asunto_consulta, 
                instancia_consulta, categoria_consulta, facultad_consulta, interesado_consulta)
    return render_to_response('buscar.html',
        {'form':form, 'resoluciones': resoluciones_resultantes, 'instancias':instancias, 'categorias':categorias, 'facultades':facultades, 'interesados':interesados},
        context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def instancias(request):
    return render_to_response('instancias.html', context_instance=RequestContext(request))

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
    return render_to_response('interesados.html',{'interesados':datos},context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def editar_interesado(request, id_interesado):
    dato = get_object_or_404(Interesado, pk=id_interesado)
    if request.method == 'POST':
        formulario = EditarInteresadoForm(request.POST, instance=dato)
        if formulario.is_valid():
            interesado_previo = formulario.save(commit=False)
            interesado_previo.registro = request.user
            interesado_previo.save()
            redireccion = "/interesados/"
            return HttpResponseRedirect(redireccion)
    else:
        formulario = EditarInteresadoForm(instance=dato)
    return render_to_response('editar_interesado.html',{'form':formulario, 'id':dato.pk}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def categorias(request):
    datos = Categoria.objects.all()
    return render_to_response('categorias.html', {'categorias':datos}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def nueva_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            categoria_previo = formulario.save(commit=False)
            categoria_previo.registro = request.user
            categoria_previo.save()
            return HttpResponseRedirect('/categorias')
    else:
        form = CategoriaForm()
    return render_to_response('nueva_categoria.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def editar_categoria(request, id_categoria):
    dato = Categoria.objects.get(pk=id_categoria)
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=dato)
        if formulario.is_valid():
            categoria_previo = formulario.save(commit=False)
            categoria_previo.registro = request.user
            categoria_previo.save()
            return HttpResponseRedirect('/categorias')
    else:
        form = CategoriaForm(instance=dato)
    return render_to_response('nueva_categoria.html', {'form':form}, context_instance=RequestContext(request))    

@login_required(login_url=login_url_variable)
def facultades(request):
    datos = Facultad.objects.all()
    return render_to_response('facultades.html',{'facultades':datos}, context_instance=RequestContext(request))

@login_required(login_url=login_url_variable)
def nueva_facultad(request):
    if request.method == 'POST':
        formulario = FacultadForm(request.POST)
        if formulario.is_valid():
            facultad_previo = formulario.save(commit=False)
            facultad_previo.registro = request.user
            facultad_previo.save()
            return HttpResponseRedirect('/facultades')
    else:
        form = FacultadForm()
    return render_to_response('nueva_facultad.html', {'form':form}, context_instance=RequestContext(request))    

@login_required(login_url=login_url_variable)
def editar_facultad(request, id_facultad):
    dato = Facultad.objects.get(pk=id_facultad)
    if request.method == 'POST':
        formulario = FacultadForm(request.POST, instance=dato)
        if formulario.is_valid():
            facultad_previo = formulario.save(commit=False)
            facultad_previo.registro = request.user
            facultad_previo.save()
            return HttpResponseRedirect('/facultades')
    else:
        form = FacultadForm(instance=dato)
    return render_to_response('nueva_facultad.html', {'form':form}, context_instance=RequestContext(request))    

def page404(request):
    return render_to_response('404.html', context_instance=RequestContext(request))

def page500(request):
    return render_to_response('500.html', context_instance=RequestContext(request))