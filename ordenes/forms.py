from django import forms
from .models import LibroPrestado

class LibroPrestadoForm(forms.ModelForm):
    class Meta:
        model = LibroPrestado
        fields = ['nombre_persona', 'identificacion', 'titulo_libro']
        widgets = {
            'nombre_persona': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Ana Gómez'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 10203040'}),
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Cien años de soledad'}),
        }