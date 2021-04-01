from django import forms
from .models import TipoDocumento, Atencion,AtencionDetalle

class TipoDocumentoForm(forms.ModelForm):
    
    class Meta:
        model = TipoDocumento
        fields = ('descripcion',)

        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class AtencionForm(forms.ModelForm):
    
    class Meta:
        model = Atencion
        fields = (
        'fechaIncidente',
        'responsable',
        'equipo',
        'detalle',
        'hora_ingreso',
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
            'fechaIncidente':forms.TextInput(
                    attrs={
                        'type':'date',
                        'class': 'form-control'
                    }
                ),
            'responsable':forms.Select(
                    attrs={
                        'class': 'form-control'
                    }
                ),
            'equipo':forms.Select(
                    attrs={
                        'class': 'form-control'
                    }
                ),
            'detalle': forms.Textarea(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'hora_ingreso':forms.TextInput(
                    attrs={
                        'type':'time',
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
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'tipoDocumento':forms.Select(
                    attrs={
                        'class': 'form-control'
                    }
                ),
        }
class AtencionDetalleForm(forms.ModelForm):
    
    class Meta:
        model = AtencionDetalle
        fields = ('pieza',
                  'cantidad',)

        widgets = {
            'pieza': forms.Select(
                attrs ={
                    'class': 'form-control'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class': 'form-control'
                }
            ),
        }



