import django_tables2 as tables

from .models import Ride
from .tables import RideTable


class RideListView(tables.SingleTableView):
    model = Ride
    table_class = RideTable
    context_object_name = 'ride_list'
    template_name = "rides/ride_list.html"
