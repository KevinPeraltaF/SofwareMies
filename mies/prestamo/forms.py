from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    """Form definition for Prestamo."""

    class Meta:
        """Meta definition for Prestamoform."""
        model = Prestamo

        fields = (
            'fecha_entrega',
            'fecha_devolucion',
            'usuario',
            'item',
            'cantidad',
            'condicion',
            'observacion',
            'estado',)
        
        widgets = {
            'fecha_entrega': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'fecha_devolucion': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'item': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'condicion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            
            'observacion': forms.Textarea(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
        }

