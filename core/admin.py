from django.contrib import admin

from core.models import *

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
# admin.site.register(Order)

@admin.register(Order)
class OrderADmin(admin.ModelAdmin):
    list_filter= ('delivered',)
admin.site.register(Cart)
admin.site.register(address)
