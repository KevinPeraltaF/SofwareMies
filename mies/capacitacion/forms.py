from django import forms
from .models import  CapacitacionCabecera




class CapacitacionForm(forms.ModelForm):
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

    def clean_areaSolicitante(self):
        data = self.cleaned_data["areaSolicitante"].upper()
        return data

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
                    'class': 'form-control'
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
            'areaSolicitante' : forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'dirigido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'instructor': forms.Select(
                attrs={
                     'class': 'form-control select'
                }
            ),
            'objetivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
           
        }
