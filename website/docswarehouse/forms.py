#encoding:utf-8
from docswarehouse.models import Instancia, Resolucion, Interesado, Facultad, Categoria
from django.forms import ModelForm
from django import forms

class InteresadoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Escribe el apellidos y nombre', 'list':'lista_interesados'}))

class EditarInteresadoForm(ModelForm):
    class Meta:
        model = Interesado
        exclude = ('registro')

class InstanciaForm(ModelForm):
    class Meta:
        model = Instancia
        exclude = ('registro')

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude = ('registro')

class FacultadForm(ModelForm):
    class Meta:
        model = Facultad
        exclude = ('registro')

class ResolucionForm(ModelForm):
    class Meta:
        model = Resolucion
        exclude = ('registro', 'interesado')

class BuscarForm(forms.Form):
    codigo = forms.CharField(
        label='Código de resolución', 
        widget=forms.TextInput(attrs={'placeholder':'ej. 01264-R-2012'}),
        required=False)
    fecha = forms.DateField(label='Fecha de emisión', required=False)
    asunto = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Algún fragmento del asunto'}), required=False)
    instancia = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la instancia', 'list':'lista_instancias'}), required=False)
    categoria = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la categoría', 'list':'lista_categorias'}), required=False)
    facultad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la facultad', 'list':'lista_facultades'}), required=False)
    interesado = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe el nombre del interesado', 'list':'lista_interesados'}),required=False)

