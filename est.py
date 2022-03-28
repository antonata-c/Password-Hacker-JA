import socket
import sys

with socket.socket() as hack_socket:
    hostname = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]

    address = (hostname, port)
    
    hack_socket.connect(address)
    hack_socket.send(message.encode())
    response = hack_socket.recv(1024).decode()
    
    print(response)






