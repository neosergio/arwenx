#encoding:utf-8
from docswarehouse.models import Instancia, Resolucion, Interesado, Facultad, Categoria
from django.forms import ModelForm
from django import forms

class InteresadoForm(forms.Form):
	nombre = forms.CharField(label='Nombre')

class InstanciaForm(ModelForm):
	class Meta:
		model = Instancia
		exclude = ('registro')

class ResolucionForm(ModelForm):
	class Meta:
		model = Resolucion
		exclude = ('registro', 'interesado')

class BuscarForm(forms.Form):
	codigo = forms.CharField(label='Código de resolución', widget=forms.TextInput(attrs={'placeholder':'ej. 01264-R-2012'}))
	fecha = forms.DateField(label='Fecha de emisión')
	asunto = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Algún fragmento del asunto'}))
	instancia = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la instancia'}))
	categoria = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la categoría'}))
	facultad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe la facultad'}))
	interesado = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Escribe el nombre del interesado', 'list':'testlist'}))

