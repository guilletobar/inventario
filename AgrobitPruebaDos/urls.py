from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from AgrobitPruebaDos.views import login_redirect
from django.contrib.auth.views import  login,logout,password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cuentas/', include('usuario.urls', namespace='cuentas')),
    url(r'^Inventario/',include('Inventario.urls', namespace='Inventario')),
    
     # Vides
    url(r'^index/$', views.index),
    url(r'^accounts/login/$', login, {'template_name': 'cuentas/login.html'},name='login'),
    url(r'^logout/$', logout, {'template_name': 'cuentas/logout.html'}, name='logout'),
    url(r'^$',views.login_redirect ),
    #cambiar clave con email ojo con los 'name' deven ser iguales
    url(r'^password_reset/', password_reset,{'template_name':'registration/password_reset_form.html',    'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'), 
    url(r'^password_reset_done/', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,  {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm' ),
    url(r'^reset/done/', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
   
]

urlpatterns += staticfiles_urlpatterns()