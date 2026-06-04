import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))
server.listen()

print("Server started...")

client, address = server.accept()
print(f"Connected to {address}")

while True:
    message = client.recv(1024).decode()
    if message.lower() == "exit":
        break

    print("Client:", message)

    reply = input("You: ")
    client.send(reply.encode())

client.close()
server.close()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

client.close()