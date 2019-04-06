import socketserver
import urllib.request
import time


def check_car(license_number):
    url = 'http://127.0.0.1:72/check/?license_number=' + license_number
    req = urllib.request.Request(url)
    return urllib.request.urlopen(req).read().decode("utf-8")


def check_card(card_number):
    url = 'http://127.0.0.1:72/check_card/?card_number=' + card_number
    req = urllib.request.Request(url)
    return urllib.request.urlopen(req).read().decode("utf-8")


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall("ACK".encode())
        while True:
            try:
                data = conn.recv(1024).decode()
                # print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
                if len(str(data)) >= 12:
                    result = check_card(str(data))
                else:
                    result = check_car(str(data))
                time.sleep(1)
                conn.sendall(result.encode())
            except ConnectionResetError:
                pass
            except Exception as e:
                pass


server = socketserver.ThreadingTCPServer(('127.0.0.1', 71), MyServer)
print("启动socketserver服务器！")
server.serve_forever()
