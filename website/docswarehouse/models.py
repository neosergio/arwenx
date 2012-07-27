from django.db import models
from django.contrib.auth.models import User

class Instancia(models.Model):
	nombre = models.CharField(max_length=255)
	registro = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)
	registro = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Facultad(models.Model):
	nombre = models.CharField(max_length=255)
	registro = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Interesado(models.Model):
	nombre = models.CharField(max_length=255, unique=True)
	registro = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Resolucion(models.Model):
	codigo_resolucion = models.CharField(max_length=13)
	fecha_emision = models.DateField()
	asunto = models.TextField()
	instancia = models.ForeignKey(Instancia)
	categoria = models.ForeignKey(Categoria)
	facultad = models.ForeignKey(Facultad, null=True, blank=True)
	interesado = models.ManyToManyField(Interesado, null=True, blank=True)
	registro = models.ForeignKey(User)

	def __unicode__(self):
		return self.codigo_resolucion

