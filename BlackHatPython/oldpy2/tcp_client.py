#!/usr/bin/env python
# coding:utf-8

# P10 TCP client
# tcp_client.py  tcp_server.py can test together.

import socket

# please first launch tcp_server.py
target_host = "127.0.0.1"    # "www.baidu.com"
target_port = 9999           # 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print response
