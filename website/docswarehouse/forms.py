from docswarehouse.models import Instancia, Resolucion, Interesado
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