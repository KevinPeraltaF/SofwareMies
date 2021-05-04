from django import forms
from .models import  Atencion,AtencionDetalle
from empleado.models import Empleado
from custodio.models import Custodio
from django.forms.models import inlineformset_factory

class AtencionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AtencionForm, self).__init__(*args, **kwargs)
        # Filtro al responsable de acuerdo a su cargo id =1; -> tics
        self.fields['responsable'].queryset = Empleado.objects.filter(estado=1, area = 1)
        #filtro para mostrar solo equipos vigentes
        self.fields['equipo'].queryset = Custodio.objects.filter(estado=1)

    class Meta:
        model = Atencion
        fields = (
        
        'responsable',
        'equipo',
        'detalle',
        'fecha_salida',
        'hora_salida',
        'instalacion',
        'configuracion',
        'prueba',
        'capacitacion',
        'hardware',
        'software',
        'observacion',
        'tipoDocumento')

        widgets = {
            
            'responsable':forms.Select(
                    attrs={
                        'class': 'form-control select'
                    }
                ),
            'equipo':forms.Select(
                    attrs={
                        'class': 'form-control select'
                    }
                ),
            'detalle': forms.Textarea(
                attrs={
                    
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'fecha_salida':forms.TextInput(
                    attrs={
                        'type':'date',
                        'class': 'form-control'
                    }
                ),
            'hora_salida':forms.TextInput(
                    attrs={
                        'type':'time',
                        'class': 'form-control'
                    }
                ),
            'instalacion':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'configuracion':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'prueba':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'capacitacion':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'hardware':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'software':forms.TextInput(
                attrs={
                    'type':'checkbox',
                    'class': 'form-group ',
                    
                }
            ),
            'observacion':forms.Textarea(
                attrs={
                  
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'tipoDocumento':forms.Select(
                    attrs={
                        'class': 'form-control select'
                    }
                ),
           
        }
class AtencionDetalleForm(forms.ModelForm):
    
    class Meta:
        model = AtencionDetalle
        fields = ('cabecera',
                   'pieza',
                  'cantidad',)

        widgets = {
            'cabecera': forms.Select(
                attrs ={
                    'class': 'form-control '
                }
            ),
            'pieza': forms.Select(
                attrs ={
                    'class': 'form-control select'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class': 'form-control'
                }
            ),
        }

AtencionCabDetalleForm = inlineformset_factory(Atencion,AtencionDetalle,
    form=AtencionDetalleForm, extra=1,can_delete= True) 