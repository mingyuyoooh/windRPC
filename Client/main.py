import rpcClient


if __name__ == '__main__':
    c = rpcClient.RPCClient()
    c.connect('127.0.0.1', 5000)        # 连接 Server
    res = c.test("测试项", kw1="1")     # 调用 Server 端的函数
    print("远程调用的返回值 res = {}".format(res))