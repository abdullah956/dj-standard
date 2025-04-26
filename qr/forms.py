from django import forms
from .models import CertificationCard


class CertificationCardForm(forms.ModelForm):
    class Meta:
        model = CertificationCard
        fields = '__all__'
        widgets = {
            'issued_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valid_until': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CertificationCardForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):  # Avoid styling checkboxes as form-control
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
