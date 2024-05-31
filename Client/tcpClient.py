import socket

"""
此文件内代码用于处理TCP的底层协议
"""
class TCPClient(object):
    def __init__(self):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='127.0.0.1', port=5000):
        """链接Server端"""
        self.clientsocket.connect((host, port))

    def send(self, data):
        """将数据发送到Server端"""
        self.clientsocket.sendall(data.encode('utf-8'))

    def receive(self, length):
        """接收Server端返回的数据"""
        r = self.clientsocket.recv(length)
        r = r.decode('utf-8')
        return r