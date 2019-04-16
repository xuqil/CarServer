"""CarServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app_api import admin
from django.urls import path
from app_api import views
from CarServer.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.admin_site.urls),
    path("push_api/", views.PushApi.as_view()),
    path("push_api_two/", views.PushApiTwo.as_view()),
    path("check/", views.check),
    path("check_card/", views.check_card),
    path("add_car/", views.add_car),
    path("add_card/", views.add_card),
    path("delete_car/", views.delete_car),
    path("delete_card/", views.delete_card),
    path("park_total", views.Pace.as_view()),
    path("park_add", views.ParkAdd.as_view()),
    path("park_subtract", views.ParkSubtract.as_view()),
    path("parkingnow/", views.ParkingNow.as_view()),
    path("entercar/", views.EnterCar.as_view()),
    path("opendoor/", views.OpenDoor.as_view()),
    path("delete_car_out", views.delete_car_out),
    path('media/<int:path>/', serve, {"document_root": MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
