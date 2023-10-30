import socket
import threading

# 创建一个客户端套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.104.130", 23))


def send_message():
    while True:
        message = input("你: ")
        client_socket.send(message.encode())


def receive_message():
    while True:
        data = client_socket.recv(1024)
        print("对方: " + data.decode())


send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
