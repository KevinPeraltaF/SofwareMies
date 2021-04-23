from django import forms
from .models import Custodio
from empleado.models import Empleado
from inventario.models import InvetarioDistritoCabecera
class CustodioForm(forms.ModelForm):
    """Form definition for AccesoRed."""
    def __init__(self, *args, **kwargs):
        super(CustodioForm, self).__init__(*args, **kwargs)
        # Filtro al responsable de acuerdo a su cargo id =1; -> tics
        self.fields['custodio'].queryset = Empleado.objects.filter(estado=1)
        #filtro que muestre solo los empleados con condicion bueno o regular excluye el id 3 -> de dañado
        self.fields['equipo'].queryset = InvetarioDistritoCabecera.objects.exclude( condicion=3)

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

