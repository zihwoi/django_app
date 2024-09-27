from django import forms
from .models import GratitudeEntry

class GratitudeForm(forms.ModelForm):
    class Meta:
        model = GratitudeEntry
        fields = ['text']
