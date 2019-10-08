from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserUpdateForm

CustomUser = get_user_model()


class CustomUserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "account/edit.html"
    success_url = reverse_lazy('home')
    success_message = _("User updated successfully")


    def get_object(self, queryset=None):
        return self.request.user
