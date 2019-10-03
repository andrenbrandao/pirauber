from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Ride


class RideForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control input-group-alternative',
            'type': 'date'
        })
    )
    time = forms.TimeField(
        required=False,
        input_formats=['%H:%M'],
        widget=forms.DateInput(attrs={
            'class': 'form-control input-group-alternative',
            'type': 'time'
        })
    )

    class Meta:
        model = Ride
        fields = ('date', 'time', 'origin', 'destination', 'seats', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', 'Save Ride', css_class='btn-block'))
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-group-alternative'
