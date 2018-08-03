from django import forms

from django.core.exceptions import ValidationError
from .models import Blogger


# class BloggerForm(forms.Form):
#     nombre = forms.CharField()
#     apellido = forms.CharField()
#     ciudad = forms.CharField()
#     email = forms.EmailField()

#     def clean_nombre(self):
#         nombre = self.cleaned_data["nombre"]

#         # El nombre posee espacios
#         if " " in nombre:
#             raise ValidationError('Nombre incorrecto -  no debe tener espacios')
#         nombre = nombre.lower()
#         return nombre


class BloggerForm(forms.ModelForm):
    def clean_nombre(self):
         nombre = self.cleaned_data["nombre"]

         # El nombre posee espacios
         if " " in nombre:
             raise ValidationError('Nombre incorrecto -  no debe tener espacios')
         nombre = nombre.lower()
         return nombre
    
    class Meta:
        model = Blogger
        fields = ["nombre", "apellido", "ciudad", "email"]
        labels = { "ciudad": "Ciudad actual" }
        help_texts = {"email" : "Ingresar un correo de contacto"}

