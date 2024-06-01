import pickle
import json
from datetime import datetime,date

"""
Server:  utilsServer.py
本文件用于存放关于各种参数与工具代码函数
"""

class CONSTANTS:
    host_server = '0.0.0.0' #服务器地址
    port_server =  5000 #服务器端口
    code_method = 'utf-8' #编码方式
    func_fname = r'windRPC\Server\func_save.jsonl'

class Tools:
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
    序列化工具函数
    """
    @staticmethod
    def load_pickle(fname:str)->pickle:
        """
        读pkl文件
        """
        with open(fname, 'rb') as f:
            return pickle.load(f)
    @staticmethod
    def dump_pickle(obj:str, fname:str)->None:
        """
        写pkl文件
        """
        with open(fname, 'wb') as f:
            pickle.dump(obj, f)
    
    
    """
    JSON工具函数
    """
    @staticmethod
    def dump_json(obj:str, fname:str)->None:
        """
        写JSON
        """
        with open(fname, 'w', encoding=CONSTANTS.code_method) as f:
            json.dump(obj, f)

    @staticmethod
    def dump_jsonl(obj:str, fname:str)->None:
        """
        写JSONL
        """
        with open(fname, 'w', encoding=CONSTANTS.code_method) as f:
            for item in obj:
                f.write(json.dumps(item) + '\n')
    
    @staticmethod
    def load_jsonl(fname:str)->list:
        """
        读JSONL
        """
        with open(fname, 'r', encoding=CONSTANTS.code_method) as f:
            lines = []
            for line in f:
                lines.append(json.loads(line))
            return lines
    

