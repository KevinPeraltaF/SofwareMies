from django import forms
from .models import Marca, Modelo, Condicion, Categoria, InventarioTics

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
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'responsable':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'ubicacion':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control',
                    "rows":3, "cols":10
                }
            ),
            'marca':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'modelo':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'condicion':forms.Select(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'serie':forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'codigoMies':forms.TextInput(
                attrs={
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'cantiad':forms.TextInput(
                attrs={
                    'type':'number',
                    'onkeyup':"javascript:this.value=this.value.toUpperCase();",
                    'class':'form-control'
                }
            ),
            'foto':forms.FileInput(
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