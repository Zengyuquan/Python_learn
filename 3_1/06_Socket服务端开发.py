import socket

# 创建Socket对象
socket_server =  socket.socket()

# 判定ip地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口
socket_server.listen(1)

# listen方法内接受一个整数传参数，表示接受的链接数量
# 等待客户端链接
#result: tuple = socket_server.accept()
#conn = result[0]        # 客户端和服务端的链接对象
#address = result[1]     # 客户端和地址信息

# 与上面三句等同
conn, address = socket_server.accept()
# accept方法返回的是二元元组(链接对象, 地址信息)
# 通过变量1 变量2 = socket_server.accept()的形式，直接接受二元元组的两个元素
# accept()方法，是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这一行不向下执行了

print(f"接收到了客户端的链接，客户端的信息是：{address}")

while True:
    # 接受客户端信息，要使用客户端和服务的的本次链接对象，而非socket_server对象
    data: str = conn.recv(1024).decode('utf-8')
    # recv接收的参数是缓冲区大小，一般1024即可
    # recv方法的返回值是关于字符数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码。将字符数组转换为字符串对象
    print(f"客户端发来的消息是：{data}")
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode('utf-8'))

# 关闭链接
conn.close()
socket_server.close()
