from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # password1 = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',            
            'email',
            'password1',
            'password2', 
            
          
        ) 
        labels = {   
            'username':'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',            
            'email':'Email',
            'password1': 'Clave',
            'password2':'Confirme clave',  
              
        }
        widgets = {
            'username':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'first_name':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'last_name':forms.TextInput(attrs={'class': 'au-input au-input--full'}),            
            'email':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'password1':forms.PasswordInput(attrs={'type': 'password'}),
            'password2':forms.PasswordInput(attrs={'type': 'password'}),
                  
        }
    def save(self,commit=True):
        user = super(RegistroForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        

        if commit:
            user.save()

        return user





class EditarPerfilForm(UserChangeForm, forms.ModelForm):
    # template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',                  
            
        )
        exclude = (
            'username',                       
        ) 
        labels = {   
            'username':'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',            
            'email':'Email',
            'password1': 'Clave',
            'password2':'Confirme clave',    
        }
        widgets = {
            'username':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'first_name':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'last_name':forms.TextInput(attrs={'class': 'au-input au-input--full'}),            
            'email':forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'password1':forms.PasswordInput(attrs={'class': 'au-input au-input--full'}),
            'password2':forms.PasswordInput(attrs={'class': 'au-input au-input--full'}),        
        }

