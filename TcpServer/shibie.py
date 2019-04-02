import urllib.request
import urllib
import base64


if __name__ == '__main__':
    try:
        from urllib import urlencode
    except ImportError:
        from urllib.parse import urlencode
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    f = open('F:\资料\广电设\CarServer\TcpServer\pictures\\timg.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {'image': img, 'image_type': 'BASE64'}
    params = urlencode(params).encode(encoding='UTF8')
    access_token = '24.ceb35ef91017dc695c08426da0fde8ed.2592000.1555846033.282335-15827027'
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read().decode('UTF-8')
    pos = content.find('number')
    if content:
        print(content[pos+10:pos+17])

