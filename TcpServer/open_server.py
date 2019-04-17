import socketserver


class MyServer(socketserver.BaseRequestHandler):
    """
    开闸TCP
    """
    def handle(self):
        conn = self.request
        while True:
            try:
                # data = conn.recv(1024).decode()
                with open("/www/wwwroot/CarServer/open.txt", 'r') as file:
                    result = file.read()
                if result == '1':
                    with open("/www/wwwroot/CarServer/open.txt", 'w') as file:
                        file.write('0')
                    conn.sendall(result.encode())
            except Exception:
                pass


server = socketserver.ThreadingTCPServer(('0.0.0.0', 71), MyServer)
print("waiting...")
server.serve_forever()
