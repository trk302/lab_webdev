from django.contrib import admin
from .models import Instrument, Order

admin.site.register(Instrument)
admin.site.register(Order)
