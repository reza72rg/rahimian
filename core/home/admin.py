from django.contrib import admin
from .models import ForeignCurrency, Client, CashIn, Broker
# Register your models here.




admin.site.register(Broker)
admin.site.register(CashIn)
admin.site.register(Client)
admin.site.register(ForeignCurrency)