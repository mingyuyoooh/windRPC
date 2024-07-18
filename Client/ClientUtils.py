import json
import argparse
from datetime import datetime

"""
Client:  ClientServer.py

本文件包含两个类：
    CONSTANTS:（用于存放参数）
    Tools: （用于存放启动参数函数以及各类工具函数）
    
"""

class CONSTANTS:
    host_registry = '127.0.0.1'#注册中心监听地址
    port_registry =  6000 #注册中心监听端口
    timeout_max = 5 #超时时间设置
    len_max = 1024 #最大接收长度
    code_method = 'utf-8'

class Tools:
    """
    注册中心启动参数
    """
    def argparser():
        """
        -h：帮助文档
        -i: 注册中心监听的ip地址
        -p: 注册中心监听的端口号
        -mxlen：客户端最大接收长度
        -mxtmo: 客户端超时时间设置
        -cdmet: 客户端编码函数
        """
        #启动参数设置
        parser = argparse.ArgumentParser(description='Client Document')
        parser.add_argument('-i', type= str, default= '127.0.0.1', help='registry listen to this ip address.')
        parser.add_argument('-p', type=int, default= 6000, help='registry listen to this port')
        parser.add_argument('-mxlen', type=int, default=1024,help = 'max recieve and send length.')
        parser.add_argument('-mxtmo', type=int, default = 10, help = 'max timeoutset of client for connection.')
        parser.add_argument('-cdmet', type=str, default = 'utf-8', help = 'client code method.')
        args = parser.parse_args()
        #启动参数加载
        CONSTANTS.host_registry= args.i
        CONSTANTS.port_registry = args.p
        CONSTANTS.len_max = args.mxlen
        CONSTANTS.timeout_max = args.mxtmo
        CONSTANTS.code_method = args.cdmet
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
    JSON工具函数
    """
    @staticmethod
    def dump_json(data:str)->json:
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
    

