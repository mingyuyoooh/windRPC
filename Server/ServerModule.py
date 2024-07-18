import json
import socket
from threading import Thread
from ServerUtils import CONSTANTS,Tools


"""
Server:  ServerModule.py

本文件包含四个类。类的继承功能如下：

TCPClient(与客户端交互)
   ->基类JSONRPC（解析函数，调用函数）
FuncRegister(存储调用函数，注册调用函数)
   ->基类TCPRegister（与注册中心交互）

"""

class JSONRPC(object):
    def __init__(self):
        self.data = None

    def from_data(self, data:json)->None:
        """解析数据"""
        try:
            self.data = Tools.load_json(data)
        except Exception as e:
            self.data = None
            print(f"[ERROR] Failed to parse data from client : {e}")
            

    def call_method(self)->dict:
        """根据解析的数据，调用对应的方法"""
        try:
            result = {}
            method_name = self.data.get('method_name', '')
            method_args = self.data.get('method_args', None)
            method_kwargs = self.data.get('method_kwargs', None)
            if method_name in self.funcs:
                res = self.funcs[method_name](*method_args, **method_kwargs)
                result['Status'] = 'Success'
                result['Info'] = res
            else:
                raise ValueError("Function Call Error")
        except Exception as e:
            print(f"[ERROR] Fail to call function: {e}")
            result['Status']= 'Fail'
            result['Info'] = str(e)
        finally:
            return result
    
    def process_request(self, data):
        self.from_data(data)
        return self.call_method()
    
    
    

class TCPClient(JSONRPC):
    def __init__(self):
        """初始化服务器TCP连接"""
        JSONRPC.__init__(self)
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(f"[ERROR] Fail to create socket: {e}")
        

    def bind_listen(self, host = CONSTANTS.host_server, port = CONSTANTS.port_server,connect_num = CONSTANTS.connect_max)->None:
        """绑定Server地址和端口"""
        try:
            self.serversocket.bind((host, port))
            self.serversocket.listen(connect_num)
        except Exception as e:
            print(f"[ERROR] Fail to bind or listen on socket: {e}")

    def receive_clientInfo(self, length=CONSTANTS.len_max):
        """接收处理请求并返回结果"""
        try:
            while True:
                clientsocket, address = self.serversocket.accept()
                client_thread = Thread(target=self.handle_client, args=(clientsocket, length))
                client_thread.start()
        except Exception as e:
            print(f"[ERROR] Fail to accept or process request: {e}")

    def handle_client(self, clientsocket:socket, length:int):
        try:
            rec = clientsocket.recv(length)
            data = Tools.dump_json(self.process_request(rec))
            clientsocket.sendall(data.encode(CONSTANTS.code_method))  
        except Exception as e:
            print(f"[ERROR] Failed to handle client: {e}")
        finally:
            clientsocket.close()

class TCPRegister(object):
    def __init__(self):
        """初始化与注册中心的TCP连接"""
        try:
            self.registersocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.registersocket.settimeout(CONSTANTS.timeout_max)
        except Exception as e:
            print(f"[ERROR] Fail to create registersocket: {e}")

    def connect_registry(self,host=CONSTANTS.host_register,port = CONSTANTS.port_register)->None:
        """链接注册中心"""
        try:
            self.registersocket.connect((host, port))
        except socket.timeout as e:
            print(f"[ERROR] connect timeout: {e}")
        except Exception as e:
            print(f"[ERROR] Fail to connect to registry: {e}")
    
    def send_registryInfo(self, data)->None:
        """将数据发送到注册中心"""
        try:
            request = Tools.dump_json(data)
            self.registersocket.sendall(request.encode(CONSTANTS.code_method))
        except socket.timeout as e:
            print(f"[ERROR] send timeout: {e}")
        except Exception as e:
            print(f"[ERROR] Fail to send data to registy: {e}")

    def receive_registryInfo(self, length = CONSTANTS.len_max)->dict:
        """接收注册中心返回的数据"""
        try:
            rec = self.registersocket.recv(length)
            return Tools.load_json(rec.decode(CONSTANTS.code_method))
        except Exception as e:
            print(f"[ERROR] Fail to receive data from registy: {e}")
            return {'Status':'Fail','Info':'Fail to receive data from registy.'}
        
    def close_registrysocket(self)->None:
        try:
            self.registersocket.close()
        except Exception as e:
            print(f"[ERROR] Failed to close register socket: {e}")

"""
Server端函数注册
"""
class FuncRegister(TCPRegister):
    def __init__(self):
        self.funcs = {}
        TCPRegister.__init__(self)
    
    def func_load(self,func,name = None)->None:
        """信息载入函数,函数被保存在funcs中"""
        try:
            if name is None:
                name = func.__name__
            self.funcs[name] = func
        except Exception as e:
            print(f"[ERROR] Fail to load function: {e}")
        

    def func_register(self)->bool:
        """
        信息注册函数,函数提交至注册中心,信息注册格式：
        {
            'Request': 注册操作，
            'ServerAddress':服务器地址，
            'ServerPort':服务器端口，
            'ValidTime':有效时间，
            'Functions':注册信息
        }
        """
        try:
            self.connect_registry()
            request_info = {'Request': 'Register','ServerAddress':CONSTANTS.host_server,'ServerPort':CONSTANTS.port_server,'ValidTime':Tools.get_stamp()+CONSTANTS.valid_time,}
            request_info['Functions'] = Tools.func2register(self.funcs)
            self.send_registryInfo(request_info)
            receive_info = self.receive_registryInfo()
            if receive_info['Status'] == 'Success':
                print(f"[INFO] Register Function Success: {receive_info['Info']}")
                return True
            elif receive_info['Status'] == 'Fail':
                print(f"[ERROR] Register Function Fail: {receive_info['Info']}")
                return False
            else:
                print(f"[ERROR] Unknown Information: {receive_info['Info']}")
                return False
        except Exception as e:
            print(f"[ERROR] Fail to register function: {e}")
            return False
        finally:
            self.close_registrysocket()
    


    

