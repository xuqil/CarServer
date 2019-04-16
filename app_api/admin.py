from .models import ParkTwo, Card, InPark, Total

from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    site_title = ugettext_lazy("校园停车场管理系统")
    site_header = ugettext_lazy("校园停车场管理系统")


admin_site = MyAdminSite()
admin_site.register(ParkTwo)
admin_site.register(Card)
admin_site.register(InPark)
admin_site.register(User)
admin_site.register(Total)
