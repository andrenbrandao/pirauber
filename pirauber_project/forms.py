from django.utils.translation import ugettext_lazy as _
from django import forms

from allauth.account.forms import LoginForm, SignupForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder, Field
from crispy_forms.bootstrap import PrependedText

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhoneNumberInternationalFallbackWidget
from intl_tel_input.widgets import IntlTelInputWidget


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('login', '<i class="ni ni-email-83"></i>'),
            PrependedText(
                'password', '<i class="ni ni-lock-circle-open"></i>'),
            Div(
                Submit('submit', _('Sign in'),
                       css_class='btn btn-primary my-4'),
                css_class='text-center'
            )
        )

    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'placeholder': _('Full Name'), 'autofocus': 'autofocus'}))
    phone = PhoneNumberField(widget=IntlTelInputWidget(allow_dropdown=True,
                                                       preferred_countries=[
                                                           'br', 'us', 'es', 'ar'],
                                                       default_code='br'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('name', '<i class="ni ni-circle-08"></i>'),
            Field('phone', css_class='input-group-alternative'),
            PrependedText('email', '<i class="ni ni-email-83"></i>'),
            PrependedText(
                'password1', '<i class="ni ni-lock-circle-open"></i>'),
            Div(
                Submit('submit', _('Sign up'),
                       css_class='btn btn-primary my-4'),
                css_class='text-center'
            )
        )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']
        user.save()
        return user
