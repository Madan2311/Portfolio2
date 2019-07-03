from django import forms 
from .models import perfil

class perfilForm(forms.ModelForm):
    class Meta:
        model = perfil 
        fields = ['nombre', 'apellido', 'telefono', 'direccion',]
        
    widgets={

            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class': 'form-control'}),

        }