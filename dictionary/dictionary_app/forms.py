from django import forms
from .models import DictionaryDB

class DictionaryForm(forms.ModelForm):
    class Meta:
        model = DictionaryDB
        fields = ['letter','word','defination','example']