from django import forms
from django.forms.models import inlineformset_factory
from .models import Marca, Modelo, Condicion, Categoria, InventarioTics, CapacidadDisco,CapacidadMemoriaRam, Procesador, InvetarioDistritoCabecera, InventarioDistritoDetalle

class InvTicsForm(forms.ModelForm):
    
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
                    'class':'form-control'
                }
            ),
            'ubicacion':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10
                }
            ),
            'marca':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'modelo':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'condicion':forms.Select(
                attrs={
                    'class':'form-control'
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
                    'class':'form-control'
                }
            )
        }
class MarcaForm(forms.ModelForm):

    class Meta:

        model = Marca
        fields = (
            'descripcion',
        )
        widgets = {
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class ModeloForm(forms.ModelForm):

    class Meta:

        model = Modelo
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class CategoriaForm(forms.ModelForm):

    class Meta:

        model = Categoria
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class CondicionForm(forms.ModelForm):

    class Meta:

        model = Condicion
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class CapacidadDiscoForm(forms.ModelForm):

    class Meta:

        model = CapacidadDisco
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
        
class CapacidadMemoriaRamForm(forms.ModelForm):

    class Meta:

        model = CapacidadMemoriaRam
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class ProcesadorForm(forms.ModelForm):

    class Meta:

        model = Procesador
        fields = (
            'descripcion',
        )
        widgets ={
            'descripcion':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
class InvetarioDistritoCabeceraForm(forms.ModelForm):
    
    class Meta:
        model = InvetarioDistritoCabecera

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
            'direccionIp',
            'direccionMac',
            'capacidadDisco',
            'capacidadMemoria',
            'capacidadProcesador',
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
                    'class':'form-control'
                }
            ),
            'ubicacion':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'class':'form-control',
                    "rows":3, "cols":10
                }
            ),
            'marca':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'modelo':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'condicion':forms.Select(
                attrs={
                    'class':'form-control'
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
            'direccionIp':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'direccionMac':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'capacidadDisco':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'capacidadMemoria':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'capacidadProcesador':forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'foto':forms.ClearableFileInput(
                attrs={
                    'type':'file',
                    'class':'form-control'
                }
            )
        }
class InventarioDistritoDetalleForm(forms.ModelForm):
    
    class Meta:
        model = InventarioDistritoDetalle

        fields = (
            'cabeceraDistrito',
            'periferico',
            'cantidad',
        )

        widgets = {
            'cabeceraDistrito': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'periferico': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'cantidad':forms.TextInput(
                attrs={
                    'type':'number',
                    'class':'form-control'
                }
            )
        } 
DetalleForm = inlineformset_factory(InvetarioDistritoCabecera,InventarioDistritoDetalle,
    form=InventarioDistritoDetalleForm, extra=4,can_delete= True) 
