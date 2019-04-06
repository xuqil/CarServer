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
from django.urls import path
from app_api.views import PushApi, PushApiTwo, check, check_card, add_car, add_card

urlpatterns = [
    path("push_api/", PushApi.as_view()),
    path("push_api_two/", PushApiTwo.as_view()),
    path("check/", check),
    path("check_card/", check_card),
    path("add_car/", add_car),
    path("add_card/", add_card),
]