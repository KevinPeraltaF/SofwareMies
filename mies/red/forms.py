from django import forms
from .models import AccesoRed

class AccesoRedForm(forms.ModelForm):
    """Form definition for AccesoRed."""
    #valido no repetidos y muestro sms de error
    def clean_direccion_mac(self):
        data = self.cleaned_data["direccion_mac"].upper()
        
        return data

    def clean_direccion_ip(self):
        data = self.cleaned_data["direccion_ip"].upper()
        
        return data

    class Meta:
        """Meta definition for AccesoRedform."""
        model = AccesoRed

        fields = (
           
            'usuario',
            'direccion_mac',
            'direccion_ip',
            'observacion',
            'estado',)
        
        widgets = {
            
            'usuario': forms.TextInput(
                attrs={
                    
                    'class': 'form-control solo-letra'
                }
            ),
            'direccion_mac': forms.TextInput(
                attrs={
                   
                    'class': 'form-control'
                }
            ),
            'direccion_ip': forms.TextInput(
                attrs={
                   
                    'class': 'form-control'
                }
            ),
            'observacion': forms.Textarea(
                attrs={
                    
                    'class': 'form-control',
                    "rows":3, "cols":10
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                   
                    'class': 'form-group ',
                  
                }
            ),
        }


   

        
