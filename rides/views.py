import datetime
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import django_tables2 as tables

from .models import Ride
from .tables import RideTable
from .forms import RideForm


class RideListView(tables.SingleTableView):
    queryset = Ride.objects.filter(
        date__gte=datetime.date.today()).order_by('date')
    table_class = RideTable
    context_object_name = 'ride_list'
    template_name = "rides/ride_list.html"
    table_pagination = {
        "per_page": 10
    }


class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    form_class = RideForm
    template_name = "rides/ride_new.html"
    success_url = reverse_lazy('ride_list')

    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)
