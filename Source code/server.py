# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5050))  # 0.0.0.0 allows connections from any IP
server_socket.listen(1)

print("Server is waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)  # Receive message
    if not data:
        break
    print("Client:", data.decode())
    reply = input("You: ")
    conn.sendall(reply.encode())  # Send reply

conn.close()
