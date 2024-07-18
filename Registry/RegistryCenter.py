import socket
from threading import Thread
import json
from RegistryUtils import Tools,CONSTANTS
from RegistryModule import RequestProcess




class RegistryCenter(RequestProcess):
    def __init__(self, host=CONSTANTS.host_registry, port=CONSTANTS.port_registry):
        self.host = host
        self.port = port
        RequestProcess.__init__(self)
    

    def start(self,connect_num = CONSTANTS.connect_max):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try: 
                print(f"[INFO] Registry Center starts at {self.host}:{self.port}")
                s.bind((self.host, self.port))
                s.listen(connect_num)
                while True:
                    conn, addr = s.accept()
                    Thread(target=self.handle_connection, args=(conn, addr)).start()
            except Exception as e:
                print(f"[ERROR] Fail to start Registry Center:{e}")



    def handle_connection(self, conn, addr):
        try:
            print(f"[INFO] Registry Center is Connected by {addr}")
            data = conn.recv(1024).decode(CONSTANTS.code_method)
            if not data:
                raise ValueError('Do not recieve any data.')
            request = Tools.load_json(data)

            response = self.process_request(request)
            conn.sendall(Tools.dump_json(response).encode(CONSTANTS.code_method))
        except Exception as e:
            print(f'[ERROR] Fail in handling connection:{e}')
        finally:
            conn.close()



