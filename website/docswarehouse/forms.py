from docswarehouse.models import Instancia, Resolucion, Interesado, Facultad
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
	facultad = forms.ModelChoiceField(queryset=Facultad.objects.all())