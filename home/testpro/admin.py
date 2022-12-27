from django.contrib import admin
from .models import Personal, Station, Train, Seat_id, Reservation, Payment

# Register your models here.
admin.site.register(Personal)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Seat_id)
admin.site.register(Reservation)
admin.site.register(Payment)
