from django import forms

class MateFormulario(forms.Form):
    tipo=forms.CharField()
    material=forms.CharField()
    
class BolsoFormulario(forms.Form):
    material=forms.CharField()
    color=forms.CharField()