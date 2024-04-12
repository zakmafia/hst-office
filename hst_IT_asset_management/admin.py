from django.contrib import admin
from .models import LaptopStore, Store, Allocation, LaptopAllocation

admin.site.register(LaptopStore)
admin.site.register(Store)
admin.site.register(Allocation)
admin.site.register(LaptopAllocation)
