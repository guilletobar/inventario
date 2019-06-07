# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone




class TipoProducto(models.Model):
    descripcion = models.TextField(max_length=20)
    
    def __str__(self):
		return '{}'.format(self.descripcion)

class Producto(models.Model):
    codigo = models.IntegerField(null=False)
    descripcion = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=50, decimal_places=5, default="")    
    cantidad = models.IntegerField(null=False)
   # fechaVencimiento = models.DateTimeField(auto_now_add=timezone.now)
   # vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    def __str__(self):
		return '{}'.format(self.codigo)

class Proveedor(models.Model):
    nombre = models.TextField(max_length=255)
    rut = models.TextField(max_length=255)
    correo = models.TextField(max_length=255)
    direccion = models.TextField(max_length=255)
    
    def __str__(self):
		return '{}'.format(self.codigo)





