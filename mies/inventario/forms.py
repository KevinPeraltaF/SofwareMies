from django import forms
from .models import Marca, Modelo, Dispositivo, CapacidadDisco,CapacidadMemoriaRam, Procesador, TipoDispositivo, TipoImpresora,TipoEquipo,ImpresoraTecnologia ,SoftwareAntivirus , SoftwareOfimatica,SistemaOperativo
from empleado.models import Empleado



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

########################

class TipoDispositivoForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = TipoDispositivo

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control ',
                    'autofocus':'autofocus'
                }
            ),
        }

class TipoImpresoraForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = TipoImpresora

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control ',
                    'autofocus':'autofocus'
                }
            ),
        }

class ImpresoraTecnologiaForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = ImpresoraTecnologia

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus '
                }
            ),
        }

class SoftwareAntivirusForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = SoftwareAntivirus

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus '
                }
            ),
        }

class SoftwareOfimaticaForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = SoftwareOfimatica

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus '
                }
            ),
        }

class SistemaOperativoForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = SistemaOperativo

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus':'autofocus'
                }
            ),
        }

class TipoEquipoForm(forms.ModelForm):
      #validaciones para que se envie como mayusculas los datos
    def clean_descripcion(self):
        data = self.cleaned_data["descripcion"].upper()
        
        return data

    class Meta:

        model = TipoEquipo

        fields = (
            'descripcion',)
        
        widgets = {
            'descripcion' : forms.TextInput(
                attrs={
                    'class': 'form-control solo-letra',
                    'autofocus':'autofocus '
                }
            ),
        }

class DispositivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipoEquipo'].empty_label = "------N/A--------"
        self.fields['marca'].empty_label = "------N/A--------"
        self.fields['modelo'].empty_label = "------N/A--------"
        self.fields['capacidadProcesador'].empty_label = "------N/A--------"
        self.fields['capacidadDisco'].empty_label = "------N/A--------"
        self.fields['capacidadMemoriaRam'].empty_label = "------N/A--------"
        self.fields['sistemaOperativo'].empty_label = "------N/A--------"
        self.fields['ofimatica'].empty_label = "------N/A--------"
        self.fields['antivirus'].empty_label = "------N/A--------"
        self.fields['tecnologia'].empty_label = "------N/A--------"
        self.fields['tipoImpresora'].empty_label = "------N/A--------"
        self.fields['tipoDispositivo'].empty_label = "------N/A--------"
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
        model = Dispositivo

        fields = (
            'categoria',
            'nombreEquipo',
            'tipoEquipo',
            'marca',
            'modelo',
            'serie',
            'codigoMies',
            'capacidadProcesador',
            'capacidadDisco',
            'capacidadMemoriaRam',
            'sistemaOperativo',
            'direccionIp',
            'direccionMac',
            'ofimatica',
            'antivirus',
            'softwareAdicional',
            'tecnologia',
            'tipoImpresora',
            'tipoDispositivo',
            'estado',
            'observacion',
            'foto'
        )

        widgets = {
            'categoria':forms.Select(
                attrs={
                    'class':'form-control select',
                    'onload':' cargar_combo() '
                }
            ),
            'nombreEquipo':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
             'tipoEquipo':forms.Select(
                attrs={
                    'class':'form-control select'
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

            'capacidadProcesador':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'capacidadDisco':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'capacidadMemoriaRam':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            
            'sistemaOperativo':forms.Select(
                attrs={
                    'class':'form-control select'
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
            'ofimatica':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'antivirus':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'softwareAdicional':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10,
                   
                }
            ),
            'tecnologia':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'tipoImpresora':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'tipoDispositivo':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
            'estado':forms.Select(
                attrs={
                    'class':'form-control select'
                }
            ),
          
            'observacion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10,
                   
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
