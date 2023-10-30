import socket
import threading

# 创建一个服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.104.130", 23))
server_socket.listen(5)

clients = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        for client in clients:
            client.send(data)

while True:
    client, addr = server_socket.accept()
    clients.append(client)
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
