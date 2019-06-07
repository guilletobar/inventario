# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
# agrega datos a  el modelo usuario de django 

class AreaTrabajo(models.Model):
        nombre = models.CharField(max_length = 100)
        descripcion = models.TextField(max_length=255)

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email')

#         user = self.model(
#             email=email,
#         )

#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.model(
#             email=email
#         )
#         user.is_admin = True
#         print(password)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user



# class User_tipos(AbstractUser):
#     is_ganaderia = models.BooleanField(default=False)
#     is_invernadero = models.BooleanField(default=False)
#     is_vides = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)


#     def get_is_ganaderia(self):
#         is_ganaderia = None
#         if hasattr(self, 'medicalprofile'):
#             is_ganaderia = self.is_ganaderia
#         return is_ganaderia

#     def get_is_invernadero(self):
#         is_invernadero = None
#         if hasattr(self, 'patientprofile'):
#             is_invernadero = self.is_invernadero
#         return is_invernadero

#     def get_is_vides(self):
#         is_vides = None
#         if hasattr(self, 'physiotherapistprofile'):
#             is_vides = self.is_vides
#         return is_vides

#     objects = MyUserManager()
#     USERNAME_FIELD = 'email'

#     @property
#     def is_staff(self):
#         return self.is_admin

#     def get_short_name():
#         return self.email


# class ganadero(models.Model):
#     user_tipos = models.OneToOneField(User_tipos, on_delete=models.CASCADE)
#     user = models.OneToOneField(User)

# class vinetero(models.Model):
#     user_tipos = models.OneToOneField(User_tipos, on_delete=models.CASCADE)
#     user = models.OneToOneField(User)

# class jardinero(models.Model):
#     user_tipos = models.OneToOneField(User_tipos, on_delete=models.CASCADE)
#     user = models.OneToOneField(User)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    rut = models.CharField(max_length = 10, default = '')
    descripcion = models.CharField(max_length = 100, default='')
    direccion =models.CharField(max_length = 100, default='')
    telefono = models.IntegerField(default=0)
    # foto = models.ImageField(upload_to='imagen_perfil',blank=True)
    

#ignorar error pylint] E1101:Class 'UserProfile' has no 'objects' member
def crear_cuenta(sender,**kwargs):
    if kwargs['created']:
        usuario_perfil= UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(crear_cuenta,sender=User)


