from django import forms
from .models import Custodio

class CustodioForm(forms.ModelForm):
    """Form definition for AccesoRed."""

    class Meta:
        """Meta definition for AccesoRedform."""
        model = Custodio

        fields = (
            'fecha',
            'custodio',
            'equipo',
            'estado',)
        
        widgets = {
            'fecha': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'custodio': forms.Select(
                attrs={
                    
                    'class': 'form-control'
                }
            ),
            'equipo': forms.Select(
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
        }

