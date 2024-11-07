# client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('server_ip_here', 5050))  # Replace 'server_ip_here' with the actual IP of the server

while True:
    message = input("You: ")
    client_socket.sendall(message.encode())  # Send message
    data = client_socket.recv(1024)  # Receive reply
    print("Server:", data.decode())

client_socket.close()
