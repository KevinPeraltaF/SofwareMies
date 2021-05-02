from django import forms
from django.forms.models import inlineformset_factory
from .models import Marca, Modelo, Condicion, Categoria, InventarioTics, CapacidadDisco,CapacidadMemoriaRam, Procesador,\
    EquipoCabecera, EquipoDetalle

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
class EquipoCabeceraForm(forms.ModelForm):
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
            'fechaIngreso': forms.TextInput(
                attrs={
                    'type':'date',
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
                    'class':'form-control select2'
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