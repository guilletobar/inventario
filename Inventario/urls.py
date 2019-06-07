from django.conf.urls import url, include
from django.contrib import admin
from Inventario.views import (
    index,
    ProductoViews,ProductoList,ProductoViewSet,ProveedorViews,ProveedorList  
    
    )

from Inventario.resources import ProductoSerializer
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from Inventario import views

router = routers.DefaultRouter()
router.register(r'api', views.ProductoViewSet)

#producto_resource = ProductoResource ()


urlpatterns = [  
   
    url(r'^$',index ),
    url(r'^', include(router.urls)),
   
    #url(r'^eliminar_vac/(?P<pk>\d+)/$',VacunaDelete.as_view(), name='eliminar_vac' ),
    
    # url(r'^pdf/',PDFprueba.as_view(), name='pdf' ),

    url(r'^agregar_pro/',ProductoViews.as_view(), name='agregar_pro' ),
    url(r'^listar_pro/',ProductoList.as_view() , name='listar_pro' ),
    #                      proveedor
    url(r'^agregar_prov/',ProveedorViews.as_view(), name='agregar_prov' ),
    url(r'^listar_prov/',ProveedorList.as_view() , name='listar_prov' ),
# APIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    
   # url(r'^admin/', admin.site.urls),
    #url(r'^api/', include(producto_resource.urls)),

]

urlpatterns += staticfiles_urlpatterns()