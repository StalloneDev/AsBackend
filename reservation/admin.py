from django.contrib import admin

from .models import Reservation, Paiement


admin.site.register((Reservation, Paiement))