from django.urls import path

from .views import RideListView, RideCreateView, RideUpdateView, RideDeleteView

urlpatterns = [
    path('', RideListView.as_view(), name='ride_list'),
    path('new/', RideCreateView.as_view(), name='ride_new'),
    path('<int:pk>/edit/', RideUpdateView.as_view(), name='ride_edit'),
    path('<int:pk>/delete/', RideDeleteView.as_view(), name='ride_delete'),
]
