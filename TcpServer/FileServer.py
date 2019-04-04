import socketserver, struct, json, os

IP = '127.0.0.1'
PORT = 8000
SERVER_ADD = (IP, PORT)


class MyTCPClass(socketserver.BaseRequestHandler):

    def get_upload(self, hander):
        file_size = hander['file_length']
        res = b''
        size = 0
        while size < file_size:
            date = self.request.recv(1024)
            size += len(date)
            res += date
        while True:
            tar_path = 'F:\资料\广电设\CarServer\TcpServer\pictures'
            if not os.path.isdir(tar_path):
                return False, '服务器,目标目录不存在'
            f_name = hander['file_name']
            f_path = os.path.join(tar_path, f_name)
            with open(f_path, 'wb')as f:
                f.write(res)
                f.flush()
            print('服务器-文件上传成功。')
            return True, '文件上传成功'

    def handle(self):
        s_hander = self.request.recv(4)
        b_hander = self.request.recv(struct.unpack('i', s_hander)[0])
        hander = json.loads(b_hander.decode('utf-8'))
        order = hander['order']
        print(hander["tar_path"])
        print(order)

        res, msg = self.get_upload(hander)
        print(msg)
        b_msg = msg.encode('utf-8')
        s_msg = struct.pack('i', len(b_msg))
        self.request.send(s_msg)
        self.request.send(b_msg)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(SERVER_ADD, MyTCPClass)
    server.serve_forever()
