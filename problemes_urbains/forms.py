from django import forms
from .models import Probleme

class ProblemeForm(forms.ModelForm):
    class Meta:
        model = Probleme
        fields = ['titre', 'description', 'categorie', 'localisation']
