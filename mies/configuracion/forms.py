from django import forms
from configuracion.models import Configuracion

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ('encargadoTics','encargadoBienes','logoIzquierdo','logocentro','logoDerecho',)

        widgets = {
            'encargadoTics' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'encargadoBienes' : forms.Select(
                attrs={
                    'class': 'form-control select'
                }
            ),
            'logoIzquierdo': forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png'
                }
            ),
            'logocentro': forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png'
                }
            ),
            'logoDerecho': forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png'
                }
            ),
        }
