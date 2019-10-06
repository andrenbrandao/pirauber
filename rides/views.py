import datetime
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.http import JsonResponse

from .models import Ride
from .tables import RideTable
from .forms import RideForm


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class RideListView(ListView):
    queryset = Ride.objects.filter(
        date__gte=datetime.date.today()).order_by('date')
    context_object_name = 'ride_list'
    template_name = "rides/ride_list.html"
    paginate_by = 5


class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    form_class = RideForm
    template_name = "rides/ride_new.html"
    success_url = reverse_lazy('ride_list')

    def form_valid(self, form):
        form.instance.driver = self.request.user
        return super().form_valid(form)


class RideUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ride
    form_class = RideForm
    template_name = "rides/ride_edit.html"
    success_url = reverse_lazy('ride_list')

    def test_func(self):
        obj = self.get_object()
        return obj.driver == self.request.user


class RideDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ride
    template_name = "rides/ride_delete.html"
    success_url = reverse_lazy('ride_list')

    def test_func(self):
        obj = self.get_object()
        return obj.driver == self.request.user
