import urllib.request


def check_car(license_number):
    url = 'http://127.0.0.1:8000/check/?license_number=' + license_number
    req = urllib.request.Request(url)
    return urllib.request.urlopen(req).read().decode("utf-8")
