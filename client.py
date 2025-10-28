import socket

host = '127.0.0.1'
port = 12345

client = socket.socket()
client.connect((host, port))

while True:
    msg = input("Client >> ")
    client.send(msg.encode())
    data = client.recv(1024).decode()
    print("Server: ", data)