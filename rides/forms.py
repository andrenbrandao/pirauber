from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils.translation import ugettext_lazy as _


from .models import Ride


class RideForm(forms.ModelForm):
    date = forms.DateField(
        label=_('Date'),
        widget=forms.DateInput(format=('%Y-%m-%d'),attrs={
            'class': 'form-control input-group-alternative',
            'type': 'date'
        })
    )
    time = forms.TimeField(
        label=_('Time'),
        required=False,
        input_formats=['%H:%M'],
        widget=forms.TimeInput(format=('%H:%M'), attrs={
            'class': 'form-control input-group-alternative',
            'type': 'time'
        })
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
        help_text=_('Write here any additional information.'),
        widget=forms.Textarea(attrs={
            'class': 'form-control input-group-alternative',
        })
    )

    class Meta:
        model = Ride
        fields = ('date', 'time', 'origin', 'destination', 'seats', 'price', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(
            Submit('submit', _('Save Ride'), css_class='btn-block'))
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input-group-alternative'
