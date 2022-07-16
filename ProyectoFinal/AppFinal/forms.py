from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioExProf(forms.Form):
    empresa = forms.CharField(max_length=40)
    puesto = forms.CharField(max_length=40)
    fechaInicial = forms.CharField(max_length=40)
    fechaFinal = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=400)
    referencia = forms.CharField(max_length=40)
    telefonoReferencia = forms.IntegerField()

class FormularioFormacion(forms.Form):
    institucion = forms.CharField(max_length=40)
    nombreCurso = forms.CharField(max_length=50)
    fechaInicial = forms.CharField(max_length=40)
    fechaFinal = forms.CharField(max_length=40)
    estado = forms.CharField(max_length=40)
    proyectoFinal = forms.CharField(max_length=100)

class FormularioSkills(forms.Form):
    software = forms.CharField(max_length=40)
    nivel = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}