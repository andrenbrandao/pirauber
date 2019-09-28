import django_tables2 as tables
from .models import Ride


class RideTable(tables.Table):
    date = tables.DateTimeColumn(format='d M Y')
    description = tables.Column()

    class Meta:
        model = Ride
        template_name = "django_tables2/bootstrap4.html"
        fields = ('date', 'time', 'origin',
                  'destination', 'driver', 'description', 'seats', 'price')
        attrs = {"class": "table table-hover"}

    def render_description(self, value, record):
        if len(value) > 30:
            return f"{value[:30]}..."
        return value
