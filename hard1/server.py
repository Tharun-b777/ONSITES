#!/usr/bin/env python3
import socket
import threading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('127.0.0.1', 8095))
sock.listen() 
while True:
    conn, addr = sock.accept()
    req = conn.recv(1024).decode('utf-8')
    conn.sendall(str.encode("HTTP/1.0 200 OK\n",'utf-8'))
    conn.sendall(str.encode('Content-Type: text/html\n\n', 'utf-8'))
    with open('index.html', 'r') as f:
        for l in f.readlines():
            print('Sent ', repr(l))
            conn.sendall(str.encode(l, 'utf-8'))
    conn.close()