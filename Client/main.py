from ClientRPC import RPCClient
from ClientUtils import Tools

"""
Client:  main.py

本文件用于执行客户端，主要功能包括：
    调用外部函数

"""

if __name__ == '__main__':
    Tools.argparser()
    c = RPCClient()
    res1 = c.test("测试项", kw1="1")     # 调用 Server 端的函数

    print("test function result = {}".format(res1))

    res2 = c.creator()

    print("creator function result = {}".format(res2))