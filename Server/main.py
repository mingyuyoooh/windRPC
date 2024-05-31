import rpcServer

"""
3.1 消息格式定义，消息序列化和反序列化（❋）
消息的格式，以及其序列化和反序列化方式可以自行定义，具体可以参考之
前我们处理 tcp 粘包的过程，另外消息的序列化和反序列化方式也可以使用其
他主流的序列化方式，如 json、xml 和 protobuf 等方式。
3.2 服务注册（❋）
RPC 服务端启动时需要注册其能支持的函数。我们要求服务端至少能同时支
持注册 10 个以上的函数。
如果你的设计中包括 “服务注册中心”，请通过它进行服务的注册。
"""



def test(*args, **kwargs):
    print("服务器端注册的 test 被调用了")
    print("test: args = {}, kwargs = {}".format(args, kwargs))
    return 'the test function has been called'


if __name__ == '__main__':
    s = rpcServer.RPCServer()
    s.register_function(test)       # 注册函数
    s.loop('127.0.0.1', 5000)       # 要监听的 IP 和端口
