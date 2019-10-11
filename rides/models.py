from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Ride(models.Model):
    created_at = models.DateTimeField(
        _("created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        _("modified"), auto_now=True, auto_now_add=False)
    driver = models.ForeignKey(get_user_model(), verbose_name=_(
        "Driver"), on_delete=models.CASCADE, related_name='rides')
    date = models.DateField(_("date"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("time"), auto_now=False,
                            auto_now_add=False, blank=True, null=True)
    origin = models.CharField(_("origin"), max_length=150)
    destination = models.CharField(_("destination"), max_length=150)
    description = models.CharField(
        _("description"), max_length=1024, blank=True)
    seats = models.IntegerField(_("seats"))
    price = models.DecimalField(
        _("price"), max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.origin} -> {self.destination}"
