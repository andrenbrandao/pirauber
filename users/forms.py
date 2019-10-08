from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder, Field, Submit
from crispy_forms.bootstrap import PrependedText

from phonenumber_field.formfields import PhoneNumberField
from intl_tel_input.widgets import IntlTelInputWidget

from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class CustomUserUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': _('Full Name'), 'autofocus': 'autofocus'}))
    phone = PhoneNumberField(widget=IntlTelInputWidget(allow_dropdown=True,
                                                       preferred_countries=[
                                                           'br', 'us', 'es', 'ar'],
                                                       default_code='br'))

    class Meta:
        model = User
        fields = ("name", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('name', '<i class="ni ni-circle-08"></i>'),
            Field('phone', css_class='input-group-alternative'),
            Div(
                Submit('submit', _('Save Account'),
                       css_class='btn btn-primary my-4 btn-block'),
                css_class='text-center'
            )
        )
