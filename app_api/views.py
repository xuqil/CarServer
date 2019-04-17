from django.http import HttpResponse
from .models import Park, AntiPark, ParkTwo, Card, InPark, Total
from django.views import View
from datetime import datetime
import time
from django.db.models import F

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


license_number_card = None
add_flag = False
add_time = None


def check(request):
    if request.method == 'GET':
        license_number = request.GET.get("license_number")
        if license_number is None:
            return HttpResponse("error")
        global license_number_card
        global add_flag
        global add_time
        add_time = time.time()
        license_number_card = license_number
        add_flag = True
        result = ParkTwo.objects.filter(license_number=license_number).first()
        if result:
            InPark.objects.create(inside=1, license_number=license_number,
                                  create_time=datetime.now())
            return HttpResponse(1)
        else:
            return HttpResponse(0)


def add_car(request):
    if request.method == 'POST':
        inside = request.POST.get("inside")
        license_number = request.POST.get("license_number")
        if inside is None or license_number is None:
            return HttpResponse("error")
        if ParkTwo.objects.filter(license_number=license_number).first() is None:
            ParkTwo.objects.create(inside=inside, license_number=license_number,
                                   create_time=datetime.now())
            return HttpResponse("添加成功")
        else:
            return HttpResponse("车牌已存在")


def add_card(request):
    if request.method == 'POST':
        card_number = request.POST.get("card_number")
        if card_number is None:
            return HttpResponse("error")
        if Card.objects.filter(card_number=card_number).first() is None:
            Card.objects.create(card_number=card_number)
            return HttpResponse("添加成功")
        else:
            return HttpResponse("已存在")


def delete_car(request):
    if request.method == 'GET':
        license_number = request.GET.get("license_number")
        if license_number is None:
            return HttpResponse("error")
        if ParkTwo.objects.filter(license_number=license_number).first() is None:
            return HttpResponse("该车牌不存在")
        else:
            ParkTwo.objects.filter(license_number=license_number).delete()
            return HttpResponse("车牌删除成功！")


def delete_card(request):
    if request.method == 'GET':
        card_number = request.GET.get("card_number")
        if card_number is None:
            return HttpResponse('error')
        if Card.objects.filter(card_number=card_number).first() is None:
            return HttpResponse(" 该卡号不存在！")
        else:
            Card.objects.filter(card_number=card_number).delete()
            return HttpResponse("卡号删除成功")


def check_card(request):
    if request.method == 'GET':
        card_number = request.GET.get("card_number")
        if card_number is None:
            return HttpResponse("error")
        result = Card.objects.filter(card_number=card_number).first()
        global add_flag
        global license_number_card
        if result:
            if add_flag and not InPark.objects.filter(license_number=license_number_card).first():
                InPark.objects.create(inside=1, license_number=license_number_card,
                                      create_time=datetime.now())
                add_flag = False
                return HttpResponse(1)
            else:
                license_number_card = None
                return HttpResponse(0)
        else:
            license_number_card = None
            return HttpResponse(0)


class ParkSubtract(View):
    def get(self, request):
        if Total.objects.filter(pk=1).first().out_park < 0:
            return HttpResponse(0)
        try:
            Total.objects.filter(pk=1).update(out_park=F("out_park") - 1)
            Total.objects.filter(pk=1).update(in_park=F("in_park") + 1)
            out_park = Total.objects.filter(pk=1).first().out_park
        except:
            return HttpResponse(0)
        return HttpResponse(out_park)


class ParkAdd(View):
    def get(self, request):
        if Total.objects.filter(pk=1).first().out_park >= 100:
            return HttpResponse(100)
        try:
            Total.objects.filter(pk=1).update(out_park=F("out_park") + 1)
            Total.objects.filter(pk=1).update(in_park=F("in_park") - 1)
            out_park = Total.objects.filter(pk=1).first().out_park
        except:
            return HttpResponse(100)
        return HttpResponse(out_park)


class Pace(View):
    def get(self, request):
        return HttpResponse(Total.objects.first().total)


class ParkingNow(View):
    def get(self, request):
        park_list = {}
        park = InPark.objects.all()
        n = 0
        for i in park:
            n += 1
            statues = dict()
            statues["IsInsideString"] = str(i.inside)
            statues["CarLicenseString"] = str(i.license_number)
            park_list[n + 1] = statues
        context = dict_to_xml(park_list, "park", "car")
        return HttpResponse(context, content_type="text/xml")


class EnterCar(View):
    def get(self, request):
        global license_number_card
        global add_time
        FreshStateString = 0
        CarLicenseString = 0
        IsInsideString = 0
        print(time.time())
        print(add_time)
        if InPark.objects.filter(license_number=license_number_card).first() and ((time.time() - add_time) <= 120):
            FreshStateString = 1
            CarLicenseString = license_number_card
            if ParkTwo.objects.filter(license_number=license_number_card).first():
                IsInsideString = 1
        status = dict()
        status["FreshStateString"] = str(FreshStateString)
        status["CarLicenseString"] = str(CarLicenseString)
        status["IsInsideString"] = str(IsInsideString)
        car_list = dict()
        car_list[1] = status
        context = dict_to_xml(car_list, "park", "car")
        return HttpResponse(context, content_type="text/xml")


class OpenDoor(View):
    def post(self, request):
        open_door = request.POST.get("opendoor")
        if open_door is None:
            return HttpResponse("error")
        if open_door == "open":
            with open("F:\资料\广电设\CarServer\open.txt", 'w') as file:
                file.write('1')
            return HttpResponse(1)
        else:
            return HttpResponse(0)


def delete_car_out(request):
    if request.method == 'GET':
        license_number = request.GET.get("license_number")
        if license_number is None:
            return HttpResponse("error")
        if InPark.objects.filter(license_number=license_number).first() is None:
            return HttpResponse("0")
        else:
            InPark.objects.filter(license_number=license_number).delete()
            return HttpResponse("1")
