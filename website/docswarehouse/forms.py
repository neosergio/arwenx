from docswarehouse.models import Instancia, Resolucion, Interesado
from django.forms import ModelForm

class InteresadoForm(ModelForm):
	class Meta:
		model = Interesado
		exclude = ('registro')

class InstanciaForm(ModelForm):
	class Meta:
		model = Instancia
		exclude = ('registro')

class ResolucionForm(ModelForm):
	class Meta:
		model = Resolucion
		exclude = ('registro')