import socket

s = socket.socket()
s.bind(('127.0.0.1', 12345))
s.listen(1)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connected", addr[0])

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"{addr[0]}: {data}")
    msg = input("Server: ")
    conn.send(msg.encode())

conn.close()