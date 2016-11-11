import socket
import threading
import msvcrt

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 100))
#global name
name = raw_input('pick your name: ')
name += ': '


def send():
    s = ''
    while s != "exit\r":
        s = ''
        x = ''
        if msvcrt.kbhit():
            while x != '\r':
                x = msvcrt.getch()
                print x,
                s += x
            print ''
            if s == "exit\r":
                client_socket.send('exit')
            else:
                client_socket.send(name + s)


def recv():
    data = ' '
    while data != "u removed from list":
        data = client_socket.recv(1024)
        print data
    client_socket.close()


threading.Thread(target=send).start()
threading.Thread(target=recv).start()
