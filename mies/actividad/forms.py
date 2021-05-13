from django import forms
from .models import  Asunto, ActividadCabecera, ActividadDetalle
from django.forms.models import inlineformset_factory


class AsuntoForm(forms.ModelForm):

  
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        return data
    def clean_observacion(self):
        data = self.cleaned_data["observacion"].upper()
        return data   
    class Meta:
        model = Asunto
        fields = ('descripcion',)

        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                        'autofocus':'autofocus'
                }
            ),
        }

class ActividadCabeceraForm(forms.ModelForm):
    
    class Meta:
        model = ActividadCabecera
        fields = (
        'fecha',
        'responsable',
        'usuario',
        'ubicacion',
        'prioridad',
        'observacion',)

        widgets = {
            'fecha':forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class': 'form-control',
                        'autofocus':'autofocus'
                }
            ),
            'responsable':forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'usuario':forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'ubicacion': forms.Select(
                attrs={
                    'class': 'form-control select',
                }
            ),
            'prioridad':forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'observacion':forms.Textarea(
                attrs={
                    
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
        }

class ActividadDetalleForm(forms.ModelForm):
    
    class Meta:
        model = ActividadDetalle
        fields = ('cabeceraActividad',
                   'asunto',)

        widgets = {
            'cabeceraActividad': forms.Select(
                attrs ={
                    'class': 'form-control'
                }
            ),
            'asunto': forms.Select(
                attrs ={
                    'class': 'form-control select',
                        'autofocus':'autofocus'
                }
            ),
        }

ActividadCabDetalleForm = inlineformset_factory(ActividadCabecera,ActividadDetalle,form=ActividadDetalleForm, extra=1,can_delete= True)