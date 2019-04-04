import socketserver
from TcpServer.request_httpt import check_car


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall("ACK".encode())
        while True:
            try:
                data = conn.recv(1024).decode()
                print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
                result = check_car(data)
                conn.sendall(result.encode())
            except ConnectionResetError:
                pass


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    print("启动socketserver服务器！")
    server.serve_forever()
