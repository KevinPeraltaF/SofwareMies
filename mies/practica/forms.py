from django import forms
from .models import Pasante, Carrera, Universidad



class PasanteForm(forms.ModelForm):
    """Form definition for Pasant."""
    class Meta:
        """Meta definition for Pasanteform."""

        model= Pasante

        fields = (
            'nombres',
            'apellidos',
            'cedula',
            'telefono',
            'carrera',
            'tutor_profesional',
            'fecha_inicio',
            'fecha_fin',
            'horas_diarias',
            'estado',
            )

        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'carrera' : forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'tutor_profesional' : forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'fecha_inicio': forms.TextInput(
                attrs={
                    'type':'date',
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'fecha_fin': forms.TextInput(
                attrs={
                    'type':'date',
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
            'horas_diarias': forms.TextInput(
                attrs={
                    'type':'number',
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
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
            }

class CarreraForm(forms.ModelForm):
    
    class Meta:

        model = Carrera

        fields = (
            'descripcion',
            'universidad',)
        
        widgets = {
            'universidad' : forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
        }

class UniversidadForm(forms.ModelForm):

     class Meta:

        model = Universidad

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control'
                }
            ),
        }





