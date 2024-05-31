import socket


class TCPServer(object):
    def __init__(self):
        # 初始化 socket；socket.AF_INET 表示因特网 IPv4 地址族，SOCK_STREAM 表示使用 TCP 的 socket 类型
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, host, port):
        # 套接字绑定的 IP 与 端口
        self.serversocket.bind((host, port))
        # 将套接字变为一个服务区套接字，进行监听，数字 5 将端口上的等待队列长度限制为 5，即超过 5 个的请求将被拒绝。
        self.serversocket.listen(5)

    def accept_receive_close(self):
        # 接收外部连接请求，当有客户端过来连接的时候, serversocket.accept 函数就会返回 2 个值
        clientsocket, address = self.serversocket.accept()
        r = clientsocket.recv(1024)
        data = self.process_request(r)
        clientsocket.sendall(data.encode('utf-8'))            # 用 sendall 发送响应给客户端
        clientsocket.close()