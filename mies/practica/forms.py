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
                    'class': 'form-control'
                }
            ),
            'apellidos': forms.TextInput(
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
          
            'carrera' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'tutor_profesional' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'fecha_inicio': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'fecha_fin': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'horas_diarias': forms.TextInput(
                attrs={
                    'type':'number',
                    'class': 'form-control',
                    'min':'1'
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),                    
            }

class CarreraForm(forms.ModelForm):
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data
    
    class Meta:

        model = Carrera

        fields = (
            'descripcion',
            'universidad',)
        
        widgets = {
            'universidad' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class UniversidadForm(forms.ModelForm):

    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Universidad

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }





