from django import forms

class MateFormulario(forms.Form):
    tipo=forms.CharField()
    material=forms.CharField()