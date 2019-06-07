# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Inventario.models import Producto,TipoProducto,Proveedor
# Register your models here.

admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Proveedor)