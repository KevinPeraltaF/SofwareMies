from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'type':'date',
                    'class': 'form-control'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
           
        }
