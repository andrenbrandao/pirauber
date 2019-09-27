from allauth.account.forms import LoginForm, SignupForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, ButtonHolder
from crispy_forms.bootstrap import PrependedText

from django.utils.translation import ugettext_lazy as _
from django import forms


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('name', '<i class="ni ni-circle-08"></i>'),
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
        user.save()
        return user
