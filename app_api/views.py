from django.http import HttpResponse
from .models import Park, AntiPark, ParkTwo
from django.views import View

from .utils import dict_to_xml


class PushApi(View):
    def get(self, request, *args, **kwargs):
        park_list = {}
        count = Park.objects.all().count()
        for i in range(count):
            statues = {}
            park_data = Park.objects.filter(park_id=i + 1).first()
            statues["CarLicenseString"] = str(park_data.license_number)
            statues["CarPostionState"] = str(park_data.status)
            if park_data.status:
                anti = AntiPark.objects.filter(license_number=park_data.license_number).first()
                if anti is not None:
                    print(anti.anti_num)
                    statues["AntiTimes"] = str(anti.anti_num)
                else:
                    statues["AntiTimes"] = str(0)
            else:
                statues["AntiTimes"] = str(0)
            park_list[i+1] = statues
        print(park_list)
        context = None
        return HttpResponse(context, content_type="text/xml")


class PushApiTwo(View):
    def get(self, request):
        park_list = {}
        count = ParkTwo.objects.all().count()
        for i in range(count):
            statues = {}
            park_data = ParkTwo.objects.filter(park_id=i + 1).first()
            statues["IsInsideString"] = str(park_data.inside)
            statues["CarLicenseString"] = str(park_data.license_number)
            park_list[i + 1] = statues
        context = dict_to_xml(park_list, "baspools", "car")
        return HttpResponse(context, content_type="text/xml")
