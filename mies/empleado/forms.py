from django import forms
from .models import Empleado, Area, Cargo, UnidadAtencion


class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""
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
            'fecha': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'area' : forms.Select(
                attrs={
                    'type': 'Select()',
                    'class': 'form-control'
                }
            ),
            'cargo' : forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'unidadAtencion' : forms.Select(
                attrs={
                    'class': 'form-control'
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
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'genero' : forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),                     
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'foto': forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'form-control'
                }
            ),
            }

class AreaForm(forms.ModelForm):
    
    class Meta:

        model = Area

        fields = (
            'descripcion',
            'distrito',)
        
        widgets = {
            'distrito' : forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CargoForm(forms.ModelForm):

     class Meta:

        model = Cargo

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class UnidadAtencionForm(forms.ModelForm):
     class Meta:

        model = UnidadAtencion

        fields = (
            'descripcion',
            'codigo',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'codigo' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }




