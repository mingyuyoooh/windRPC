本作业只要符合以下所有要求，具体使用什么方法、什么设计思路，同学们可以
自由发挥。标有红色 ❋ 的必须实现或遵循，这是 RPC 最基本的功能。标有（可
选，加分项）的是选做内容，完成后可适当加分，具体参考“五、评分标准”。
3.1 消息格式定义，消息序列化和反序列化（❋）
消息的格式，以及其序列化和反序列化方式可以自行定义，具体可以参考之
前我们处理 tcp 粘包的过程，另外消息的序列化和反序列化方式也可以使用其
他主流的序列化方式，如 json、xml 和 protobuf 等方式。
3.2 服务注册（❋）
RPC 服务端启动时需要注册其能支持的函数。我们要求服务端至少能同时支
持注册 10 个以上的函数。
如果你的设计中包括 “服务注册中心”，请通过它进行服务的注册。
3.3 服务发现（❋）
RPC 服务器需要为客户端提供接口，这样客户端才能知道服务端是否支持其
希望调用的服务。
如果你的设计中包括 “服务注册中心”，请通过它进行服务的发现。
3.4 服务调用（❋）
在 RPC 客户端发现服务后，根据你所设置的 RPC 协议正确地调用远程服
务。服务调用的输入和输出的数据格式即在 3.1 你定义的格式。
3.5 服务注册中心（可选，加分项）
可以支持多个服务端把自己的服务注册到服务注册中心，客户端向服务注册
中心询问服务端的地址并调用。
3.6 支持并发（❋）
服务端需要具有并发处理客户端请求的能力。
比如，假设客户端 A 发来请求，然后服务端处理客户端 A 的请求，这时客
户端 B 也发来了请求，要求服务端也能同时处理客户端 B 的请求，不能出现服
务端处理完客户端 A 的请求才能处理客户端 B 的请求的情况，导致客户端 B
需要等待。具体地，可以利用多线程或者多进程的方式，参考我们之前的编程作
业！
另外，我们要求，服务端至少可以支持并发处理 10 个客户端的请求。
3.7 异常处理及超时处理（❋）
RPC 框架需要具备进行异常处理以及超时处理的能力。其中，超时处理包括
但不限于以下几个方面。
（1）客户端处理异常/超时的地方：
 与服务端建立连接时产生的异常/超时
 发送请求到服务端，写数据时出现的异常/超时
 等待服务端处理时，等待处理导致的异常/超时（比如服务端已挂死，
迟迟不响应）
 从服务端接收响应时，读数据导致的异常/超时
（2）服务端处理异常/超时的地方：
 读取客户端请求数据时，读数据导致的异常/超时
 发送响应数据时，写数据导致的异常/超时
 调用映射服务的方法时，处理数据导致的异常/超时
3.8 负载均衡（可选，加分项）
为了减少服务端的负载，服务端肯定不能只有一个，客户端可以通过服务注
册中心选择服务器。因此，负载均衡功能就是把每个请求平均负载到每个服务器
上，充分利用每个服务器的资源。
注：考虑成本原因，不同的服务器可以使用多个虚拟机或 docker 镜像，但
不能是单机多线程或多进程。
3.9 其他要求(❋，包括 3.9.* )
3.9.1 编程语言选择
我们限定编程语言为：C、C++、Java、Python 和 Golang。另外，为了让同学
们更容易上手实现，我们提供一个 C 语言版本的基本代码框架供大家参考，具体
可以查看代码里的注释，已经写得比较清楚
3.9.2 写明运行教程
你需要在设计文档中详细说明程序的运行教程，包括客户端和服务端。
服务端的启动参数必须至少包括：
1）-h，帮助参数，输出参数帮助，具体格式可以自行定义，清晰易懂即可
2）-l，服务端监听的 ip 地址，需要同时支持 IPv4 和 IPv6，可以为空，默
认监听所有 ip 地址，即 0.0.0.0
3）-p，服务端监听的端口号，不得为空
客户端的启动参数必须至少包括：
1）-h，帮助参数，输出参数帮助，具体格式可以自行定义
2）-i，客户端需要发送的服务端 ip 地址，需要同时支持 IPv4 和 IPv6，
不得为空
3）-p，客户端需要发送的服务端端口，不得为空。
比如，以 C,C++,或其他编译型语言（直接编译成可执行文件）为例子的客户
端和服务端的启动命令：
服务端：./server -l 192.168.3.1 -p 2333
客户端：./client -i 192.168.3.1 -p 233
3.9.3 不能利用现有框架或第三方库（除了消息序列化和反序列化外）
除了消息序列化和反序列化外，不得使用任何现有的框架或第三方库。当然操
作系统和语言本身提供的库（非第三方库）是允许使用的，比如 socket 编程，我们
需要用到类 Unix 的 POSIX 接口去实现。除此之外的功能必须由你们自己设计并实
现。
3.9.4 禁止抄袭
代码不得相互抄袭。一些设计思路可以相互借鉴，但代码必须自己实现。我们会
对代码进行查重处理（包括本课程开课以来历届同学所提交的所有代码），若经我
们查重 + 二次人工确认后，发现有 严重 抄袭行为，抄袭者和被抄袭者双方，本大
作业直接 0 分处理！
3.10 协作加分项（可选，加分项）
为了鼓励同学们更加深入了解RPC，并让框架达到企业级的水平，我们设置
了一个加分项：
几位同学之间共同设计同一套RPC协议，每个同学分别用不同的编程语言去实
现（注意：不是同一种编程语言实现同一套RPC协议的多个实现版本）。需要实
现跨语言之间的相互调用（比如同学 A 用 Java语言实现了客户端 client，同
学B用C语言实现了服务端，客户端可以通过共同定义的RPC协议调用服务端的服
务），否则不视为同一套RPC协议，不参与加分。
注：上述任何加分项需在代码、设计文档及其他文件中明确体现，否则不予加分。