from ClientModule import InfoProcess



"""
Client:  ClientRPC.py

本文件包含核心类RPCClient。该类继承的类包括：

InfoProcess(发现函数与调用函数)

RPCClient的核心函数为__getattr__(将调用函数转为调用请求)

"""

class RPCClient(InfoProcess):
    def __getattr__(self, item):
        def func(*args, **kwargs):
            request = {
                'method_name': item,
                'method_args': args,
                'method_kwargs': kwargs
            }
            return self.FunctionCallProcess(request) 
            # return self.InfoProcess(request,'127.0.0.1',5000)        
        setattr(self, item, func)
        return func
