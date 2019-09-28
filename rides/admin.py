from django.contrib import admin
from .models import Ride


class RideAdmin(admin.ModelAdmin):
    list_display = ('date', 'driver', 'origin',
                    'destination', 'created_at', 'updated_at',)


admin.site.register(Ride, RideAdmin)
