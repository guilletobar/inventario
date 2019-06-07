from django import forms
from Inventario.models import Producto,TipoProducto,Proveedor


class DateInput(forms.DateInput):
    input_type = 'date'
    

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = [
            'descripcion',
             
        ] 
        labels = {
            'descripcion':'Descripcion',
        }
        widgets = { 'descripcion':forms.TextInput(attrs={'class': 'input-group-addon'}) , }




class ProductoForm(forms.ModelForm):
      class Meta:
        model=Producto
        fields = [            
            'codigo',
            'descripcion',
            'peso',
            'cantidad',
            #'fechaVencimiento',
        ]
        labels = {            
            'codigo':'Codigo',
            'descripcion':'Tipo de producto',
            'peso':'Peso',
            'cantidad':'Cantidad',
            #'fechaVencimiento':'FechaVencimiento',
                       
        }
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            #'fechaVencimiento':forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class ProveedorForm(forms.ModelForm):
      class Meta:
        model=Proveedor
        fields = [            
            'nombre',
            'rut',
            'correo',
            'direccion',
            #'fechaVencimiento',
        ]
        labels = {            
            'nombre':'Nombre',
            'rut':'Rut',
            'correo':'Correo',
            'direccion':'Direccion',
            #'fechaVencimiento':'FechaVencimiento',
                       
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'form-control'}) ,
            'rut':forms.TextInput(attrs={'class': 'form-control'}) ,
            'correo':forms.EmailInput(attrs={'class': 'form-control'}) ,
            'direccion':forms.TextInput(attrs={'class': 'form-control'}) ,
        }









# class AnimalForm(forms.ModelForm):
#     class Meta:
#         model = Animal
#         fields = {'diio',
#         'especie',}
#         labels = {  
#             'diio' : 'correlativo' ,             
#             'especie':'Especie',    
#         }
#         widgets = {
#             'diio':forms.TextInput(attrs={'class': 'form-control'}) ,           
#             'especie': forms.Select(),  
#         }
        # def AgregarAnimales_1(request):
        #     model = Animal	
        #     PuertoSerie = serial.Serial('COM8', 9600)
        #         # Creamos un buble sin fin
        #     # template_name = 'ganaderia/animal_agregar.html'
        #     # while True:
        #     # leemos hasta que encontarmos el final de linea
        #     sArduino = PuertoSerie.readline()
        #     # Mostramos el valor leido y eliminamos el salto de linea del final
        #     print "Valor Arduino: " + sArduino.rstrip('\n')
        #     nfc = sArduino.rstrip
        #     # xdxd = {'model':model}
        #     contexto = {'nfc':nfc,'model':model}	
        #     return render(request, 'ganaderia/animal_agregar.html',contexto)
        #     # return { "form": form}

