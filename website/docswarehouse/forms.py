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
	instancia = forms.ModelChoiceField(queryset=Instancia.objects.all())
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
	facultad = forms.ModelChoiceField(queryset=Facultad.objects.all())
	interesado = forms.ModelChoiceField(queryset=Interesado.objects.all())

