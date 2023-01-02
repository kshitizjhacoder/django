from django.contrib import admin
from .models import Personal, Station, Train, Reservation, Payment, Cld

# Register your models here.
admin.site.register(Personal)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Cld)

admin.site.register(Reservation)
admin.site.register(Payment)
