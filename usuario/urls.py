from django.conf.urls import url, include
from usuario.views import registrar,home,perfil,editar_perfil,cambiar_clave
from django.contrib.auth.views import  password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^$', home, name='home'),
    # url(r'^login/$', login, {'template_name': 'cuentas/login.html'},name='login'),
    # url(r'^logout/$', logout, {'template_name': 'cuentas/logout.html'}, name='logout'),
    url(r'^registrar/$', registrar, name='registrar'),
    url(r'^perfil/$', perfil, name='perfil'),
    url(r'^perfil/editar/$', editar_perfil, name='editar_perfil'),
    url(r'^cambiar-clave/$', cambiar_clave, name='cambiar_clave'),
    
]
