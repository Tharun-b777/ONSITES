#!/usr/bin/env python3
import socket
import threading 
s=socket.socket() 

s.bind(('0.0.0.0',9045))

s.listen()
clients=[]
def connections(connection):
    while True:
        message=connection.recv(1024)
        print(message.decode('utf-8'))
        try:
            for client in clients:
                client.send(message)
        except:
            clients.remove(connection)
            connection.close()
            break
    
while True:
    conn,addr=s.accept()
    print(conn)
    Thread1=threading.Thread(target=connections,args=(conn,))
    clients.append(conn)
    Thread1.start()


