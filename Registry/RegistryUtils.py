import json
import argparse
from datetime import datetime

"""
Registry:  RegistryUtils.py

本文件包含两个类：
    CONSTANTS:（用于存放参数）
    Tools: （用于存放启动参数函数以及各类工具函数）
"""

class CONSTANTS:
    host_registry = '127.0.0.1' #注册中心监听地址
    port_registry =  6000 #注册中心端口
    valid_time = 60 # 注册函数有效时间
    len_max = 1024 #最大接收长度
    connect_max = 10 #最大连接数量
    timeout_max = 10 #超时时间设置
    code_method = 'utf-8' #编码方式

class Tools:
    """
    注册中心启动参数
    """
    def argparser():
        """
        -h：帮助文档
        -i: 注册中心监听的ip地址
        -p: 注册中心监听的端口号
        -mxval: 函数有效注册时间
        -mxlen: 最大接收参数
        -mxcon: 注册中心最大连接数量
        -mxtmo: 注册中心超时时间
        -cdmet: 注册中心编码函数
        """
        #启动参数设置
        parser = argparse.ArgumentParser(description='Registry Document')
        parser.add_argument('-i', type= str, default= '127.0.0.1', help='registry listen to this ip address.')
        parser.add_argument('-p', type=int, default= 6000, help='registry listen to this port')
        parser.add_argument('-mxval', type=int, default= 60, help='function max valid time in registry .')
        parser.add_argument('-mxlen', type=int, default=1024,help = 'max recieve and send length.')
        parser.add_argument('-mxcon', type=str, default= 10, help='max connection of registry.')
        parser.add_argument('-mxtmo', type=int, default = 10, help = 'max timeoutset of registry for connection.')
        parser.add_argument('-cdmet', type=str, default = 'utf-8', help = 'registry code method.')
        args = parser.parse_args()
        #启动参数加载
        CONSTANTS.host_registry = args.i
        CONSTANTS.port_registry = args.p
        CONSTANTS.valid_time = args.mxval
        CONSTANTS.len_max = args.mxlen
        CONSTANTS.connect_max = args.mxcon
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
    def dump_json(data:str)->dict:
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

