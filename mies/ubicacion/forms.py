from django import forms
from .models import Zona , Provincia, Distrito

class ZonaForm(forms.ModelForm):
    """Form definition for Zona."""
    #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        return data

    class Meta:
        """Meta definition for Zonaform."""
        model = Zona

        fields = (
            'descripcion',
            )
        
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
    
    
class ProvinciaForm(forms.ModelForm):
    """Form definition for provincia."""
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        return data
    
    class Meta:
        """Meta definition for provincia."""
        model = Provincia

        fields = (
            'zona',
            'descripcion'
            )
        
        widgets = {
            'zona': forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class DistritoForm(forms.ModelForm):
    """Form definition for Distrito."""

     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        return data
       
    class Meta:
        """Meta definition for Distrito."""
        model = Distrito

        fields = (
            'provincia',
            'descripcion',
            )
        
        widgets = {
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
    