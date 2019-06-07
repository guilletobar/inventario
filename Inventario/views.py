# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from Inventario.models import Producto,TipoProducto,Proveedor
from Inventario.forms import ProductoForm,TipoProductoForm,ProveedorForm
from django.views.generic import ListView, UpdateView,CreateView,DeleteView, TemplateView,View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
# import serial
from django.contrib.messages.views import SuccessMessageMixin
# PDF
# from AgrobitPruebaDos.pdf_creador import render_pdf

from rest_framework import viewsets
from Inventario.resources import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all()#.order_by('-date_joined')
    serializer_class = ProductoSerializer

# Create your views here.

def index(request):
    return render(request,'Inventario/index_Inventario.html')


class ProductoViews(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'Inventario/producto_add.html'
	success_url = reverse_lazy('Inventario:listar_pro')

class ProductoList(ListView):
    model = Producto
    template_name = 'Inventario/producto_list.html'
    paginate_by = 5	

class ProveedorViews(CreateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'Inventario/proveedor_add.html'
	success_url = reverse_lazy('Inventario:listar_prov')

class ProveedorList(ListView):
    model = Proveedor
    template_name = 'Inventario/proveedor_list.html'
    paginate_by = 5

# class FichaMedicaUpdate(UpdateView):
# 	model = FichaMedica
# 	form_class = FichaMedicaForm
# 	template_name = 'Inventario/ficha_medica.html'
# 	success_url = reverse_lazy('Inventario:listar_fm')

# class FichaMedicaDelete(DeleteView):
# 	model = FichaMedica
# 	template_name = 'eliminar_ficha.html'
# 	success_url = reverse_lazy('Inventario:listar_fm')

# AMIKNAL


# pdf metodos

# class PDFprueba(View):
# 	def get(self,request,*arg,**kwargs):
# 		mascota = FichaMedica.objects.all().order_by('id')
		
# 		contexto = {'mascotas':mascota,'user':request.user}
# 		pdf = render_pdf("pdf/pdf_archivo.html", contexto)			
# 		return HttpResponse(pdf, content_type = "application/pdf")

	

# def AgregarAnimales_1(request):
# 	model = Animal	
# 	PuertoSerie = serial.Serial('COM8', 9600)
# 		# Creamos un buble sin fin
# 	# template_name = 'Inventario/animal_agregar.html'
# 	# while True:
# 	# leemos hasta que encontarmos el final de linea
# 	sArduino = PuertoSerie.readline()
# 	# Mostramos el valor leido y eliminamos el salto de linea del final
# 	print "Valor Arduino: " + sArduino.rstrip('\n')
# 	nfc = sArduino.rstrip
# 	# xdxd = {'model':model}
# 	contexto = {'nfc':nfc,'model':model}	
# 	return render(request, 'Inventario/agregar_nfc.html',contexto)
#     # return { "form": form}
