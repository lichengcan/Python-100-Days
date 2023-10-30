import socket
import threading

# 创建客户端socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
server_address = ('192.168.104.130', 23)  # 请将服务器IP地址替换为实际的服务器地址
client_socket.connect(server_address)


# 处理接收消息
def receive():
    while True:
        try:
            # 接收消息
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            # 出现错误时关闭客户端
            print("与服务器断开连接")
            client_socket.close()
            break


# 启动接收消息的线程
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 发送消息
while True:
    message = input()
    client_socket.send(message.encode('utf-8'))
