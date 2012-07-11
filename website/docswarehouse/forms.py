from docswarehouse.models import Instancia
from django.forms import ModelForm

class InstanciaForm(ModelForm):
	class Meta:
		model = Instancia
		exclude = ('registro')