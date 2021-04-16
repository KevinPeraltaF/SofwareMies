from django import forms
from .models import AccesoRed

class AccesoRedForm(forms.ModelForm):
    """Form definition for AccesoRed."""

    class Meta:
        """Meta definition for AccesoRedform."""
        model = AccesoRed

        fields = (
            'fecha',
            'usuario',
            'direccion_mac',
            'direccion_ip',
            'observacion',
            'estado',)
        
        widgets = {
            'fecha': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'usuario': forms.TextInput(
                attrs={
                    
                    'class': 'form-control'
                }
            ),
            'direccion_mac': forms.TextInput(
                attrs={
                   
                    'class': 'form-control'
                }
            ),
            'direccion_ip': forms.TextInput(
                attrs={
                   
                    'class': 'form-control'
                }
            ),
            'observacion': forms.Textarea(
                attrs={
                    
                    'class': 'form-control',
                    "rows":3, "cols":10
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

