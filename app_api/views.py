from django.http import HttpResponse
from .models import Park, AntiPark, ParkTwo, Card
from django.views import View
from datetime import datetime

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
        park = ParkTwo.objects.all()
        n = 0
        for i in park:
            n += 1
            statues = dict()
            statues["IsInsideString"] = str(i.inside)
            statues["CarLicenseString"] = str(i.license_number)
            park_list[n + 1] = statues
        context = dict_to_xml(park_list, "park", "car")
        return HttpResponse(context, content_type="text/xml")


def check(request):
    license_number = request.GET.get("license_number")
    result = ParkTwo.objects.filter(license_number=license_number).first()
    if result:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


def add_car(request):
    inside = request.POST.get("inside")
    license_number = request.POST.get("license_number")
    if ParkTwo.objects.filter(license_number=license_number).first() is None:
        ParkTwo.objects.create(inside=inside, license_number=license_number,
                               create_time=datetime.now())
        return HttpResponse("添加成功")
    else:
        return HttpResponse("车牌已存在")


def add_card(request):
    card_number = request.POST.get("card_number")
    if Card.objects.filter(card_number=card_number).first() is None:
        Card.objects.create(card_number=card_number)
        return HttpResponse("添加成功")
    else:
        return HttpResponse("已存在")


def delete_car(request):
    license_number = request.GET.get("license_number")
    if ParkTwo.objects.filter(license_number=license_number).first() is None:
        return HttpResponse("该车牌不存在")
    else:
        ParkTwo.objects.filter(license_number=license_number).delete()
        return HttpResponse("车牌删除成功！")


def delete_card(request):
    card_number = request.GET.get("card_number")
    if Card.objects.filter(card_number=card_number).first() is None:
        return HttpResponse(" 该卡号不存在！")
    else:
        Card.objects.filter(card_number=card_number).delete()
        return HttpResponse("卡号删除成功")


def check_card(request):
    card_number = request.GET.get("card_number")
    result = Card.objects.filter(card_number=card_number).first()
    if result:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

