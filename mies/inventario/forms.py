from django import forms
from django.forms.models import inlineformset_factory
from .models import Marca, Modelo, Condicion, Categoria, InventarioTics, CapacidadDisco,CapacidadMemoriaRam, Procesador,\
    EquipoCabecera, EquipoDetalle
from empleado.models import Empleado

class InvTicsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvTicsForm, self).__init__(*args, **kwargs)
        # Filtro al responsable de acuerdo a su cargo id =1; -> tics
        #self.fields['responsable'].queryset = Empleado.objects.filter(cargo=1)

     #validaciones para que se envie como mayusculas los datos
    def clean_serie(self):
        data = None
        try:
            data = self.cleaned_data["serie"].upper()
        except:
            pass
        
        return data
    
    def clean_codigoMies(self):
        data = None
        try:
            data = self.cleaned_data["codigoMies"].upper()
        except:
            pass
        return data

    class Meta:
        model = InventarioTics

        fields = (
            'fechaIngreso',
            'responsable',
            'ubicacion',
            'categoria',
            'descripcion',
            'marca',
            'modelo',
            'condicion',
            'serie',
            'codigoMies',
            'cantidad',
            'foto'
        )

        widgets = {
            'fechaIngreso': forms.TextInput(
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'responsable':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'ubicacion':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10,
                    'autofocus':'autofocus'
                }
            ),
            'marca':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'modelo':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'condicion':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'serie':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'codigoMies':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class':'form-control',
                    'min':'0'
                }
            ),
            'foto':forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png',
                    
                }
            )
        }
class MarcaForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Marca
        fields = (
            'descripcion',
        )
        widgets = {
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class ModeloForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Modelo
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class CategoriaForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Categoria
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class CondicionForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Condicion
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class CapacidadDiscoForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = CapacidadDisco
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
        
class CapacidadMemoriaRamForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = CapacidadMemoriaRam
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class ProcesadorForm(forms.ModelForm):
     #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = Procesador
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'autofocus':'autofocus'
                }
            )
        }
class EquipoCabeceraForm(forms.ModelForm):

      #validaciones para que se envie como mayusculas los datos
    def clean_serie(self):
        data = None
        try:
            data = self.cleaned_data["serie"].upper()
        except:
            pass
        
        return data
    
    def clean_codigoMies(self):

        data = None
        try:
             data = self.cleaned_data["codigoMies"].upper()
        except:
            pass
        
        return data
       
     
    
    def clean_direccionIp(self):
        data = None
        try:
             data = self.cleaned_data["direccionIp"].upper()
        except:
            pass
        
        return data

        
   
    def clean_direccionMac(self):
        data = None
        try:
             data = self.cleaned_data["direccionMac"].upper()
        except:
            pass
        
        return data

  
    class Meta:
        model = EquipoCabecera

        fields = (
            'fechaIngreso',
            'categoria',
            'descripcion',
            'marca',
            'modelo',
            'condicion',
            'serie',
            'codigoMies',
            'direccionIp',
            'direccionMac',
            'capacidadDisco',
            'capacidadMemoria',
            'capacidadProcesador',
            'foto'
        )

        widgets = {
            'fechaIngreso': forms.DateInput(format=('%Y-%m-%d'),
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10,
                    'autofocus':'autofocus'
                }
            ),
            'marca':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'modelo':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'condicion':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'serie':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'N/A'
                }
            ),
            'codigoMies':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'N/A'
                }
            ),
            'direccionIp':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'N/A'
                }
            ),
            'direccionMac':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'N/A'
                }
            ),
            'capacidadDisco':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'capacidadMemoria':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'capacidadProcesador':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'foto':forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class': 'dropify',
                    'data-allowed-file-extensions':'jpg jpeg JPEG JPG png'
                }
            )
        }
class EquipoDetalleForm(forms.ModelForm):
    class Meta:
        model = EquipoDetalle

        fields = (
            'cabeceraDistrito',
            'periferico',
            'cantidad',
        )
        widgets = {
            'periferico': forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control select'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class':'form-control'
                }
            )
        }
EquipoCabDetalleForm = inlineformset_factory(EquipoCabecera,EquipoDetalle,
    form=EquipoDetalleForm, extra=1,can_delete= True) 