import socket
import sys
import itertools


args = sys.argv
n = 0

with socket.socket() as client_socket:
    with open('/Users/antonzemtsov/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt', 'r') as file:
        passwords = file.read().split()
        host = args[1]
        port = int(args[2])
        address = (host, port)
        client_socket.connect(address)
        while True:
            password = map(lambda x: ''.join(x),
                           itertools.product(*([letter.lower(), letter.upper()] for letter in passwords[n])))
            n += 1
            for word in password:
                message = word.encode()
                client_socket.send(message)
                response = client_socket.recv(1024)
                response = response.decode()
                if response == "Connection success!":
                    print(word)
                    exit()
