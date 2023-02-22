from django.contrib import admin

from .models import Uav, UavBrand, UavCategory, UavCompany

admin.site.register(Uav)
admin.site.register(UavCompany)
admin.site.register(UavBrand)
admin.site.register(UavCategory)
