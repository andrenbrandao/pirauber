from django.urls import path
from .views import CustomUserUpdateView

urlpatterns = [
    path('edit/', CustomUserUpdateView.as_view(), name='account_edit'),
]
