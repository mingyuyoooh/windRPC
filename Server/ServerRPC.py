import socket
from concurrent.futures import ThreadPoolExecutor
from ServerUtils import CONSTANTS
from ServerModule import TCPClient, FuncRegister

"""
Server:  ServerRPC.py

本文件包含核心类RPCServer。该类继承的类包括：

TCPClient(封装了与客户端交互的函数)
FuncRegister(封装了与注册中心交互的函数)

RPCServer的核心函数为loop(循环收发信息)

"""

class RPCServer(TCPClient, FuncRegister):
    def __init__(self) -> None:
        TCPClient.__init__(self)
        FuncRegister.__init__(self)

    def loop(self, host=CONSTANTS.host_server, port=CONSTANTS.port_server, max_workers=CONSTANTS.max_worker) -> None:
        self.bind_listen(host, port)
        print(f'[INFO] Server start at {host}:{port}.')
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while True:
                executor.submit(self.receive_clientInfo)

    def bind_listen(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(CONSTANTS.connect_max)
        print(f'[INFO] Listening on {host}:{port}')
