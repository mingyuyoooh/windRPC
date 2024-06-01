import json
import tcpServer

from utilsServer import CONSTANTS,Tools

"""
Server端函数注册
"""
class funcRegister(object):
    def __init__(self):
        self.funcs = self.load_funcs()
    #TODO 加入No，拓展为多服务器
    def register_function(self, fn)->None:
        """
        注册函数以JSONL格式存储
        =======================
        {
            name:函数名称
            createdTime:
            serverAddress:
            serverPort:
        }
        =======================
        """
        func = {}
        func['name'] = fn.__name__
        func['createdTime'] = Tools.get_time()
        func['serverAddress'] = CONSTANTS.host_server
        func['serverPort'] = CONSTANTS.port_server
        self.funcs[fn.__name__] = func
    
    def save_funcs(self)->None:
        """
        存储注册函数,文件路径存放于utilsServer.py
        """
        Tools.dump_jsonl(self.funcs,CONSTANTS.func_fname)
    
    def load_funcs(self)->dict:
        """
        读取注册函数,文件路径存放于utilsServer.py
        """
        func_list = Tools.load_jsonl(CONSTANTS.func_fname)
        return {index: func for index, func in enumerate(func_list)}

    

