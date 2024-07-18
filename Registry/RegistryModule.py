from random import randint
from threading import Lock
from RegistryCenter import CONSTANTS,Tools

class InfoProcess:
    def __init__(self):
        self.funcs = {} # 存储服务信息
        self.lock = Lock()

    def FuncRegister(self, request:dict)->dict:
        """
        信息注册函数,服务器信息注册请求格式：
        
        {
            'Request': 注册操作，
            'ServerAddress':服务器地址，
            'ServerPort':服务器端口，
            'ValidTime':有效时间，
            'Functions':注册信息
        }
        """
        try:
            print('[INFO] Start to register functions.')
            ServerAddress = request.get('ServerAddress')
            ServerPort = request.get('ServerPort')
            ValidTime = request.get('ValidTime')
            Funcs = request.get('Functions')
            ServerInfo = (ServerAddress,ServerPort)
            with self.lock:
                self.funcs[ServerInfo] = {'ValidTime':ValidTime,'Functions':Funcs}
            return {'Status': 'Success','Info':'Succcessful Function Registration!'}
        except Exception as e:
            print(f'[ERROR] Fail to Register Functions:{e}')
            return {'Status': 'Error', 'message': 'Wrong Request!'}
        

    def load_balancing(self,func_list:list)->tuple:
        try:
            return func_list[randint(0,len(func_list)-1)]
        except Exception as e:
            print(f'[ERROR] Fail to load balancing:{e}')
            return None
    
    def FuncDiscover(self, request:dict)->dict:
        """
        获取服务
        """
        try:
            with self.lock:
                func_name = request.get('Info')
                print(f'[INFO] start to discover function {func_name}')
                func_discover = []
                for server , registerInfo in self.funcs.items():
                    registerFuncs = registerInfo.get('Functions')
                    if func_name in registerFuncs:
                        func_discover.append(server)
                if len(func_discover) > 0:
                    server_select = self.load_balancing(func_discover) 
                    return {'Status': 'Success', 'Info':{'host_server': server_select[0],'port_server': server_select[1]}}
                else:
                    print(f'[ERROR] Do not discover function {func_name}')
                    return {'Status': 'Fail', 'Info': 'Do not discover relevant function!'}
        except Exception as e:
            print(f'[ERROR] Fail in discover {func_name}:{e}')
            return {'Status': 'Fail', 'Info': f'Fail in discovering function:{e}'}






    


            
class RequestProcess(InfoProcess):
    def __init__(self) -> None:
        InfoProcess.__init__(self)
        
    
    def process_request(self, request:dict)->dict:
        try:
            print(f"[INFO] Start to process request.")
            Request = request.get('Request')

            if Request == 'Register':
                return self.FuncRegister(request)
            elif Request == 'Discover':
                return self.FuncDiscover(request)
            else:
                return {'Status': 'Fail', 'Info': 'Unknown action'}
        except Exception as e:
            print(f"[ERROR] Fail to process request:{e}")



