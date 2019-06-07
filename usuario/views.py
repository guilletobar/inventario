# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.shortcuts import render, redirect
from usuario.forms import RegistroForm,EditarPerfilForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def home(request):
    args = {'user':request.user}
    return render(request, 'base_pagina.html',args)


def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form=RegistroForm()

    args = {'form':form }
    return render(request,'cuentas/registro_usuario.html', args)

def perfil(request):
    args = {'user':request.user}
    return render(request, 'cuentas/perfil.html',args)

def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        
        if form.is_valid():
            
            form.save()
            return redirect(reverse('cuentas:perfil'))
    else:
        form = EditarPerfilForm(instance=request.user)
        args = {'form': form}
        return render(request, 'cuentas/editar_perfil.html', args)


def cambiar_clave(request):
    if request.method == 'POST':
        form = PasswordChangeForm( data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('cuentas:perfil'))
        else:
            return redirect(reverse('cuentas:cambiar_clave'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'cuentas/cambiar_clave.html', args)