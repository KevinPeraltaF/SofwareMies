from django import forms
from .models import Prestamo
from inventario.models import InventarioTics

class PrestamoForm(forms.ModelForm):
    """Form definition for Prestamo."""
    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
      
        self.fields['item'].queryset = InventarioTics.objects.exclude(cantidad =0 )
        

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
            'fecha_entrega': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'autofocus':'autofocus'
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
                    'class': 'form-control select'
                }
            ),
            'item': forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min':'0'
                }
            ),

            'condicion': forms.Select(
                attrs={
                    'class': 'form-control select'
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
                    
                }
            ),
        }

