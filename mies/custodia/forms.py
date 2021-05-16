from django import forms
from .models import Custodia
from empleado.models import Empleado
from inventario.models import Dispositivo
class CustodiaForm(forms.ModelForm):
    """Form definition for AccesoRed."""
    def __init__(self, *args, **kwargs):
        super(CustodiaForm, self).__init__(*args, **kwargs)
        # Filtro al responsable de acuerdo a su cargo id =1; -> tics
        self.fields['custodio'].queryset = Empleado.objects.filter(estado=1)
        self.fields['categoria'].empty_label = "------N/A--------"
        #filtro que muestre solo los empleados con condicion bueno o regular excluye el id 3 -> de dañado
        #self.fields['equipo'].queryset = Dispositivo.objects.exclude( estado=3)
       
    categoria = forms.ChoiceField(label=u"Categoria", choices=[('1', 'COMPUTADORAS'),('2', 'IMPRESORAS'), ('3', 'OTROS DISPOSITIVOS'),], required=False, widget=forms.Select(attrs={'class': 'form-control select'}))
        
    class Meta:
        """Meta definition for AccesoRedform."""
        model = Custodia
        #extra field -no estan directamente en el modelo
        
        

        fields = (
            'fecha',
            'custodio',
            'custodioAnterior',
            'equipo',
            'estado',)
        
        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class': 'form-control'  
                    }
            ),
            'custodio': forms.Select(
                attrs={
                    
                    'class': 'form-control select'
                }
            ),
            'custodioAnterior': forms.Select(
                attrs={
                    
                    'class': 'form-control ',
                    'disabled':'True',
                    
                }
            ),
         
            'equipo': forms.Select(
                attrs={
                   
                    'class': 'form-control select'
                }
            ),
      
            'estado': forms.CheckboxInput(
                attrs={
                   
                    'class': 'form-group ',
                  
                }
            ),
        }

