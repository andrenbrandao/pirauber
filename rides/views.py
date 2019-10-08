import datetime
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from django.http import JsonResponse

from .models import Ride
from .tables import RideTable
from .forms import RideForm


class RideListView(ListView):
    queryset = Ride.objects.filter(
        date__gte=datetime.date.today()).order_by('date')
    context_object_name = 'ride_list'
    template_name = "rides/ride_list.html"
    paginate_by = 5


class RideCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ride
    form_class = RideForm
    template_name = "rides/ride_new.html"
    success_url = reverse_lazy('ride_list')
    success_message = _("Ride created successfully")

    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)


class RideUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Ride
    form_class = RideForm
    template_name = "rides/ride_edit.html"
    success_url = reverse_lazy('ride_list')
    success_message = _("Ride updated successfully")

    def test_func(self):
        obj = self.get_object()
        return obj.driver == self.request.user


class RideDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ride
    template_name = "rides/ride_delete.html"
    success_url = reverse_lazy('ride_list')
    success_message = _("Ride deleted successfully")

    def test_func(self):
        obj = self.get_object()
        return obj.driver == self.request.user

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response
