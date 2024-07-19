import json
import argparse
from datetime import datetime

"""
Server:  ServerUtils.py

本文件包含两个类：
    CONSTANTS:（用于存放参数）
    Tools: （用于存放启动参数函数以及各类工具函数）

"""

class CONSTANTS:
    host_server = '127.0.0.1' #服务器监听地址
    port_server =  5000 #服务器监听端口
    host_register = '127.0.0.1'#注册中心地址
    port_register =  6000 #注册中心端口
    valid_time = 60 # 注册函数有效时间
    len_max = 1024 #最大接收长度
    connect_max = 10 #最大连接数量
    timeout_max = 10 #超时时间设置
    code_method = 'utf-8' #编码方式
    max_worker = 10 #最大工作数量

class Tools:

    """
    服务端启动参数
    """
    def argparser():
        """
        -h：帮助文档
        -i: 服务器监听的ip地址
        -p: 服务器监听的端口号
        -ri:注册中心监听的ip地址
        -rp:注册中心监听的端口号
        -mxval: 函数有效注册时间
        -mxlen: 最大接收参数
        -mxcon: 服务器最大连接数量
        -mxtmo: 服务器超时时间
        -cdmet: 服务器编码函数
        """
        #启动参数设置
        parser = argparse.ArgumentParser(description='Server Document')
        parser.add_argument('-i', type= str, default= '127.0.0.1', help='server listen to this ip address.')
        parser.add_argument('-p', type=int, default=5000, help='server listen to this port')
        parser.add_argument('-ri', type=str, default= '127.0.0.1', help='registry address.')
        parser.add_argument('-rp', type=int, default = 6000, help = 'registry port.')
        parser.add_argument('-mxval', type=int, default= 60, help='function max valid time in registry .')
        parser.add_argument('-mxlen', type=int, default=1024,help = 'max recieve and send length.')
        parser.add_argument('-mxcon', type=str, default= 10, help='max connection of server.')
        parser.add_argument('-mxtmo', type=int, default = 10, help = 'max timeoutset of server for connection.')
        parser.add_argument('-cdmet', type=str, default = 'utf-8', help = 'server code method.')
        parser.add_argument('-mxwrk', type=int, default = 10, help = 'server max worker.')
        args = parser.parse_args()
        #启动参数加载
        CONSTANTS.host_server = args.i
        CONSTANTS.port_server = args.p
        CONSTANTS.host_register =args.ri
        CONSTANTS.port_register = args.rp
        CONSTANTS.valid_time = args.mxval
        CONSTANTS.len_max = args.mxlen
        CONSTANTS.connect_max = args.mxcon
        CONSTANTS.timeout_max = args.mxtmo
        CONSTANTS.code_method = args.cdmet
        CONSTANTS.max_worker = args.mxwrk

    """
    时间工具函数
    """
    @staticmethod
    def stamp_to_time(stamp:int)->str:
        """
        时间戳->时间
        """
        dateTime = datetime.fromtimestamp(stamp)
        return dateTime.strftime('%Y-%m-%d %H:%M:%S')
    @staticmethod
    def time_to_stamp(dateTime:datetime)->int:
        """
        时间->时间戳
        """
        return dateTime.timestamp()
    @staticmethod
    def get_time()->str:
        """
        获取当前时间
        """
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    @staticmethod
    def get_stamp()->str:
        """
        获取当前时间戳
        """
        return datetime.now().timestamp()
    

    """
    信息转化函数
    """
    @staticmethod
    def func2register(fn:dict)->dict:
        """
        函数转为字典形式存储,用于向注册中心注册函数字典格式：
        {
            name:函数名称
            args:函数参数
            funcinfo：函数信息
        }
        """
        func_container = {}
        for name , func in fn.items():
            func_container[name] = {'name':func.__name__,'args':func.__code__.co_varnames,'info':func.__doc__}
        return func_container
    
    
    """
    JSON工具函数
    """
    @staticmethod
    def dump_json(data:str)->None:
        """
        写JSON
        """
        return json.dumps(data, ensure_ascii=False, indent=4)
            

    @staticmethod
    def load_json(data:str)->dict:
        """
        读JSON
        """
        return json.loads(data)
    

