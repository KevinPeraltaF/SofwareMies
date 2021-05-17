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
                    'class': 'form-control solo-numero',
                    'autofocus':'autofocus'
                }
            ),
        }
    
    
class ProvinciaForm(forms.ModelForm):
    """Form definition for provincia."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zona'].empty_label = "------N/A--------"
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
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus'
                }
            ),
        }


class DistritoForm(forms.ModelForm):
    """Form definition for Distrito."""
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provincia'].empty_label = "------N/A--------"
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        return data

    def clean_alias(self):
        data = self.cleaned_data["alias"].upper()
        return data
       
    class Meta:
        """Meta definition for Distrito."""
        model = Distrito

        fields = (
            'provincia',
            'descripcion',
            'alias',
            )
        
        widgets = {
            'provincia': forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus'
                }
            ),
             'alias': forms.TextInput(
                attrs={
                    'class': 'form-control',
                 
                }
            ),
        }
    