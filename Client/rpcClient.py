import json
import tcpClient


class RPCStub(object):
    def __getattr__(self, item):
        def func(*args, **kwargs):
            d = {
                'method_name': item,
                'method_args': args,
                'method_kwargs': kwargs
            }
            self.send(json.dumps(d))        # 发送数据到 Server 端
            return self.receive(1024)       # 接收 Server 返回的执行结果

        setattr(self, item, func)
        return func


class RPCClient(tcpClient.TCPClient, RPCStub):
    pass