from django import forms
from .models import Pasante, Carrera, Universidad
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe




class PasanteForm(forms.ModelForm):       
    """Form definition for Pasant."""
    #extra field -no estan directamente en el modelo
    universidad = forms.ModelChoiceField(
         queryset= Universidad.objects.all(), 
         widget= forms.Select( attrs={
                    'class': 'form-control select'
                }
            ))




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tutor_profesional'].empty_label = "------N/A--------"
        self.fields['carrera'].empty_label = "------N/A--------"
        self.fields['universidad'].empty_label = "------N/A--------"
       
      
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
                    'class': 'form-control solo-letra'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra'
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
                    'class': 'form-control solo-numero',
                    'min':'1'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control select'
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
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus'
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
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus'
                }
            ),
        }





