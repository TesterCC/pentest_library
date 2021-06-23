#!/usr/bin/env python
# coding:utf-8

# P12

import socket
import threading


bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listning on %s:%d" % (bind_ip, bind_port)

# There is client handle thread

def handle_client(client_socket):
    # print client send and get content
    request = client_socket.recv(1024)

    print "[*] Recevied: %s" % request

    # return a data
    client_socket.send("ACK!")

    client_socket.close()


while True:

    client, addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    # hang up client thread, handle input data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()



