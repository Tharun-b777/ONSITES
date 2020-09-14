#!/usr/bin/env python3
import socket
import threading
so=socket.socket()
print(so)
so.connect(('0.0.0.0',9045))
name=input("Enter name ")
def sent():
    while True:
        message='{}:{}'.format(name,input(''))
        so.send(message.encode('utf-8')) 
def rcv():
    while True:
        try:
            data=so.recv(1024).decode('utf-8')
            print(data)
        except:
            print("Error")
            so.close()
            break

reciev=threading.Thread(target=rcv)
sen=threading.Thread(target=sent)
reciev.start()
sen.start()
