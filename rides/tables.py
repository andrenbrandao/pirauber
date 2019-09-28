import django_tables2 as tables
from .models import Ride


class RideTable(tables.Table):
    date = tables.DateTimeColumn(format='d M Y')

    class Meta:
        model = Ride
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'origin',
                  'destination', 'driver')
