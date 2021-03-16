from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
  class Meta:
    model=Mascota

    fields =[
      'nombre',
      'sexo',
      'edad_aproximada',
      'fecha_recate',
      'persona',
      'vacuna',

    ]
    labels={
      'nombre': 'Nombre',
      'sexo': 'Sexo',
      'edad_aproximada': 'Edad aproximada',
      'fecha_recate':'Fecha Rescate',
      'persona': 'Adoptante',
      'vacuna': 'Vacuna',
    }
    widget={
      'nombre':forms.TextInput(attrs={'class':'form-control'}),
      'sexo':forms.TextInput(attrs={'class':'form-cpmtrol'}),
      'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
      'fecha_recate':forms.DateField(),
      'persona':forms.Select(attrs={'class':'form-control'}),
      'Vacuna': forms.CheckboxSelectMultiple(),

    }