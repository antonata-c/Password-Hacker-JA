import itertools
import socket
import sys

from string import ascii_lowercase, digits

args = sys.argv
with socket.socket() as client_socket:
    client_socket.connect((args[1], int(args[2])))
    alphabet = ascii_lowercase + digits
    for count in range(1, len(alphabet) + 1):
        for password in itertools.product(alphabet, repeat=count):
            data = ''.join(password).encode()
            client_socket.send(data)
            response = client_socket.recv(1024).decode()
            if response == 'Connection success!':
                print(data.decode())
                exit()