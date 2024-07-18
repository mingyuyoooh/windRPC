from ServerRPC import RPCServer
from ServerFuncs import *
from ServerUtils import CONSTANTS,Tools


"""
Server:  main.py

本文件用于执行服务端，主要功能包括：
    启动参数加载；
    函数加载和注册；
    客户端信息接收与处理

"""

if __name__ == "__main__":

    # 启动参数加载
    Tools.argparser()

    s = RPCServer()       
    #基本计算函数
    # s.func_load(add)
    # s.func_load(minus)
    # s.func_load(mul)
    # s.func_load(div)
    #基本时间操作函数
    # s.func_load(time_to_stamp)
    # s.func_load(stamp_to_time)
    # s.func_load(get_time)
    # s.func_load(get_stamp)
    #测试与输出函数
    s.func_load(creator)
    s.func_load(test)
    
    # 注册函数
    s.func_register()

    # 监听信息
    s.loop()       
