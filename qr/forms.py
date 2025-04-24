from django import forms
from .models import CertificationCard

class CertificationCardForm(forms.ModelForm):
    class Meta:
        model = CertificationCard
        fields = '__all__'
        widgets = {
            'issued_on': forms.DateInput(attrs={'type': 'date'}),
            'valid_until': forms.DateInput(attrs={'type': 'date'}),
        }
