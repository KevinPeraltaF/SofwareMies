from django import forms
from .models import  CapacitacionCabecera, CapacitacionDetalle

from django.forms.models import inlineformset_factory


class CapacitacionCabeceraForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_tema(self):
        data = self.cleaned_data["tema"].upper()
        return data

    def clean_lugar(self):
        data = self.cleaned_data["lugar"].upper()
        return data
    
    def clean_objetivo(self):
        data = self.cleaned_data["objetivo"].upper()
        return data

    def clean_dirigido(self):
        data = self.cleaned_data["dirigido"].upper()
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['areaSolicitante'].empty_label = "------N/A--------"
       

    class Meta:

        model = CapacitacionCabecera
        fields = (
            'fecha',
            'hora_inicio', 
            'hora_fin' ,
            'lugar' ,
            'tema',
            'tipoCapacitacion', 
            'areaSolicitante' ,
            'dirigido', 
            'instructor', 
            'objetivo',
            )

   
        
        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'autofocus':'autofocus'
                }
            ),
            'hora_inicio': forms.TextInput(
                attrs={
                    'type':'time',
                    'class': 'form-control'
                }
            ),
            'hora_fin' : forms.TextInput(
                attrs={
                    'type':'time',
                    'class': 'form-control'
                }
            ),
            'lugar' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tema': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipoCapacitacion': forms.Select(
                attrs={
                     'class': 'form-control select'
                }
            ), 
            'areaSolicitante' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'dirigido': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra'
                }
            ),
            'instructor': forms.Select(
                attrs={
                     'class': 'form-control select'
                }
            ),
            'objetivo': forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra'
                }
            ),
           
        }


class CapacitacionDetalleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empleado'].empty_label = "------N/A--------"
   
    class Meta:

        model = CapacitacionDetalle
        fields = (
            'capacitacionCabecera',
            'empleado',
            'observacion', 
                    
            )
        
        widgets = {
            'empleado': forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class': 'form-control select'
                }
            ),
            'observacion':forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "rows":1, "cols":10
                }
            ),
        }

CapacitacionCabDetalleForm = inlineformset_factory(CapacitacionCabecera,CapacitacionDetalle,
    form=CapacitacionDetalleForm, extra=1,can_delete= True) 
