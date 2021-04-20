from django import forms
from .models import Prioridad, Asunto, ActividadCabecera, ActividadDetalle
from django.forms.models import inlineformset_factory

class PrioridadForm(forms.ModelForm):
    
    class Meta:
        model = Prioridad
        fields = ('descripcion',)

        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class AsuntoForm(forms.ModelForm):
    
    class Meta:
        model = Asunto
        fields = ('descripcion',)

        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
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
            'fecha':forms.TextInput(
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
            'usuario':forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'ubicacion': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'prioridad':forms.Select(
                attrs={
                    'class': 'form-control'
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
                    'class': 'form-control'
                }
            ),
        }

DetalleForm = inlineformset_factory(ActividadCabecera,ActividadDetalle,form=ActividadDetalleForm, extra=1,can_delete= True)