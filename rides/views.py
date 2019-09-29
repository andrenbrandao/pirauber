import datetime
import django_tables2 as tables

from .models import Ride
from .tables import RideTable


class RideListView(tables.SingleTableView):
    queryset = Ride.objects.filter(
        date__gte=datetime.date.today()).order_by('date')
    table_class = RideTable
    context_object_name = 'ride_list'
    template_name = "rides/ride_list.html"
    table_pagination = {
        "per_page": 10
    }
