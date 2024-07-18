from RegistryUtils import Tools
from RegistryCenter import RegistryCenter

"""
Registry:  main.py

本文件用于执行注册中心，主要功能包括：
    启动参数加载；
    接收客户端和服务端请求
    
"""

if __name__ == '__main__':
    Tools.argparser()
    s = RegistryCenter()       # 注册函数
    s.start()
