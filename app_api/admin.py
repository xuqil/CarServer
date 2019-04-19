from .models import ParkTwo, Card, InPark, Total, OpenOrder

from django.utils.translation import ugettext_lazy
from django.contrib import admin


class ParkTwoAdmin(admin.ModelAdmin):
    list_display = ('park_id', 'inside', 'license_number', 'create_time')


class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'card_number')


class InParkAdmin(admin.ModelAdmin):
    list_display = ('park_id', 'inside', 'license_number', 'create_time')


class TotalAdmin(admin.ModelAdmin):
    list_display = ('in_park', 'out_park', 'total')


class OpenOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order')


admin.site.site_title = ugettext_lazy("校园停车场管理系统")
admin.site.site_header = ugettext_lazy("校园停车场管理系统")
admin.site.register(ParkTwo, ParkTwoAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(InPark, InParkAdmin)
admin.site.register(Total, TotalAdmin)
admin.site.register(OpenOrder, OpenOrderAdmin)
