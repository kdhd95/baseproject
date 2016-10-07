import socket
import threading

server_socket=socket.socket()
server_socket.bind(('0.0.0.0', 100))
server_socket.listen(10)

clients_list=[]

def play_client():
    global clients_list
    data1=''
    (client_socket, address) = server_socket.accept()
    clients_list.append(client_socket)
    while data1!='exit':
        data1=client_socket.recv(1024)
        print data1
        if data1=="exit":
            clients_list.remove(client_socket)
            client_socket.send('u removed from list')
        else:
            for i in clients_list:
                if i!= client_socket:
                    i.send(data1)
                
#main
for i in range (10):
    threading.Thread(target=play_client).start()

