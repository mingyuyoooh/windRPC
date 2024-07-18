import socket

from ClientUtils import Tools,CONSTANTS


"""
Client:  ClientModule.py

本文件包含两个类，其继承关系与功能如下：

InfoProcess(发现函数与调用函数)
    ->继承TCPClient(与注册中心和服务端交互)

"""

    
class TCPClient(object):
    def __init__(self)->None:
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.settimeout(CONSTANTS.timeout_max)

    def connect(self, host, port)->None:
        """连接地址"""
        try:
            address = (host, port)
            self.clientsocket.connect(address)
        except socket.timeout as e:
            print(f"[ERROR] Connect timeout: {e}")
        except Exception as e:
            print(f"[ERROR] Fail to connect: {e}")

    def send(self, data:dict, code_method = CONSTANTS.code_method)->None:
        """发送数据"""
        try:
            request = Tools.dump_json(data)
            self.clientsocket.sendall(request.encode(code_method))
        except socket.timeout as e:
            print(f"[ERROR] send timeout: {e}")
        except Exception as e:
            print(f"[ERROR] Fail to send data: {e}")
        

    def receive(self, length = CONSTANTS.len_max, code_method = CONSTANTS.code_method)->dict:
        """接收返回数据"""
        try:
            rec = self.clientsocket.recv(length).decode(code_method)
            return Tools.load_json(rec)
        except Exception as e:
            print(f"[ERROR] Fail to receive data from registy: {e}")
            return {'Status':'Fail','Info':'Fail to receive data.'}
    
    def close(self)->None:
        """关闭端口"""
        try:
            self.clientsocket.close()
        except Exception as e:
            print(f"[ERROR] Fail to close register socket: {e}")


class InfoProcess():
    def __init__(self):
        pass
        

    def InfoProcess(self,data:dict,host_server:str,port_server:int):
        """发送请求，接收结果，处理结果"""
        try:
            infoClient = TCPClient()
            infoClient.connect(host_server,port_server)
            infoClient.send(data)
            rec = infoClient.receive()
            status = rec.get('Status')
            info = rec.get('Info')
            if status == 'Success':
                return info
            elif status == 'Fail':
                raise ValueError(f'Fail Status due to {info}')
        except Exception as e:
            print(f"[ERROR] Fail to process request: {e}")
            return None
        finally:
            infoClient.close()

    def FunctionCallProcess(self,data:dict,host_registry = CONSTANTS.host_registry, port_registry = CONSTANTS.port_registry):
        """
        向注册中心发送发现函数请求，向服务端发送调用函数请求,格式:
        {
            'Request':'Discover',
            'Info':函数信息，
        }
        """
        try:
            print('[INFO] Discover Function From Registry.')
            request = {'Request': 'Discover','Info': data.get('method_name')}
            info = self.InfoProcess(request,host_registry,port_registry)
            if info is None:
                raise ValueError('Fail to recieve registry data')
            else:
                print('[INFO] Call Function From Server.')
                host_server, port_server = info.get('host_server'),info.get('port_server')
                rec = self.InfoProcess(data,host_server,port_server)
                return rec
        except Exception as e:
            print(f"[ERROR] Fail to process function call request: {e}")

            
        








