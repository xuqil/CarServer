import socketserver
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from TcpServer.DB.DatabaseModel import OpenOrder
import time

engine = create_engine('sqlite:///F:\资料\广电设\CarServer\db.sqlite3', encoding='utf8')
DBSession = sessionmaker(engine)
session = DBSession()


class MyServer(socketserver.BaseRequestHandler):
    """
    开闸TCP
    """
    def handle(self):
        conn = self.request
        while True:
            try:
                time.sleep(3)
                print("ok")
                result = session.query(OpenOrder).filter(OpenOrder.order_id == 1).first().order
                print(result)
                if result:
                    session.query(OpenOrder).filter(OpenOrder.order_id == 1).update({'order': 0})
                    session.commit()
                    print("ok2")
                    conn.sendall(str(result).encode())
            except Exception:
                pass


server = socketserver.ThreadingTCPServer(('0.0.0.0', 71), MyServer)
print("waiting...")
server.serve_forever()
