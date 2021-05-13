from django import forms
from .models import Empleado, Area, Cargo, UnidadAtencion


class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""
     #validaciones para que se envie como mayusculas los datos
    def clean_correo(self):
        data = self.cleaned_data["correo"].upper()
        return data
    
    
    class Meta:
        """Meta definition for Empleadoform."""

        model= Empleado

        fields = (
            'fecha',
            'area',
            'cargo',
            'unidadAtencion',
            'estado',
            'nombres',
            'apellidos',
            'genero',
            'correo',
            'cedula',
            'telefono',
            'foto',)

        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'area' : forms.Select(
                attrs={
                    
                    'class': 'form-control select'
                }
            ),
            'cargo' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'unidadAtencion' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    'checked':'True',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra'
                }
            ),
            'genero' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),                     
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control solo-numero'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control solo-numero'
                }
            ),
            'foto': forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png'
                }
            ),
            }

class AreaForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data
    
    class Meta:

        model = Area

        fields = (
            'descripcion',
            'distrito',)
        
        widgets = {
            'distrito' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus':'autofocus'
                }
            ),
        }

class CargoForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Cargo

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus':'autofocus'
                }
            ),
        }

class UnidadAtencionForm(forms.ModelForm):

     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = UnidadAtencion

        fields = (
            'descripcion',
            'codigo',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus':'autofocus'
                }
            ),
            'codigo' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }




