from django.urls import path

from .views import RideListView, RideCreateView

urlpatterns = [
    path('', RideListView.as_view(), name='ride_list'),
    path('new/', RideCreateView.as_view(), name='ride_new'),
]
