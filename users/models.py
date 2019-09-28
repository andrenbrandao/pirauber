from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    name = models.CharField(_("Name"), blank=True, max_length=255)
    phone = PhoneNumberField(_("Phone"), blank=True)

    def __str__(self):
        return self.name
