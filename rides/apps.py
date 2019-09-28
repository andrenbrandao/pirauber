from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class RidesConfig(AppConfig):
    name = 'rides'
    verbose_name = _("Rides")
