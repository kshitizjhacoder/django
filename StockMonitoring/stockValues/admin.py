from django.contrib import admin
from .models import Stock, Promotor_holding, Price, PNL
# Register your models here.
admin.site.register(Stock)
admin.site.register(Promotor_holding)
admin.site.register(Price)
admin.site.register(PNL)
