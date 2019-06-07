#from tastypie.resources import ModelResource
#from ganaderia.models import Producto
#from tastypie.authorization import Authorization

#class ProductoResource(ModelResource):
#    class Meta:
#        queryset = Producto.objects.all()
#        resource_name = 'producto' 
#        authorization = Authorization ()
#        always_return_data = True
#        TASTYPIE_ALLOW_MISSING_SLASH  =  True
#        TASTYPIE_DEFAULT_FORMATS  =  [ 'json' ]
        #fields = ['codigo','descripcion','peso','cantidad']
from Inventario.models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo',
        'descripcion',
        'peso',
        'cantidad']