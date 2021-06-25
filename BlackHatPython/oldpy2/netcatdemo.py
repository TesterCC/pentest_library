#!/usr/bin/env python
# coding:utf-8

# blackhat P14-P21

import os
import sys
import socket
import getopt
import threading
import subprocess

# print(os.path.basename(__file__))   # get current filename
# print(os.path.basename(sys.argv[0]))
script_name = os.path.basename(__file__)


# define some global variable
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def useage():
    print(">>>>>>>MFC Pentest Net Tool<<<<<<<")
    print("")
    print("Usage: {0} -t target_host -p port".format(script_name))
    print("")
    print("-l --listen                 - listen on [host]:[port] for incomming connections")
    print("-e --execute=file_to_run    - execute the given file upon receiving a connection")
    print("-c --command                - initialize a command shell")
    print("-u --upload=destination     - upon receiving connection upload a file and write to [destination]")
    print("")
    print("Examples: ")
    print("{0} -t 192.168.0.1 -p 5555 -l -c".format(script_name))
    print("{0} -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe".format(script_name))
    print("{0} -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"".format(script_name))
    print("echo 'ABCDEFGHI' | ./{0} -t 192.168.11.12 -p 135".format(script_name))
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        useage()

    # get command -var
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hel:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        useage()

    for o, a in opts:
        if o in ("-h", "--help"):
            useage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    # 是进行监听还是仅从标准输入发送数据？
    if not listen and len(target) and port > 0:

        # 从命令行读取内存数据
        # 这里将阻塞，所以不再向标准输入发送数据时发送CTRL-D
        # 模仿netcat从标准输入中读取数据，并通过网络发送数据
        buffer = sys.stdin.read()

        # send data
        client_sender(buffer)

    # 我们开始监听并准备上传文件、执行命令
    # 放置一个反弹shell
    # 取决于上面的命令行选项
    if listen:
        server_loop()


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接到目标主机
        client.connect((target, port))

        if len(buffer):
            client.send(buffer)

        while True:
            # 现在等待数据回传
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print(response)

            # 等待更多的输入
            buffer = input("")
            buffer += "\n"

            # 发送出去
            client.send(buffer)

    except:

        print("[*]Exception! Exiting.")
        # close connection
        client.close()


def server_loop():
    global target

    # 如果没有定义目标,那么我吗监听所有接口
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))

    server.listen(5)    # 最大监听数

    # while True:   # P18


if __name__ == '__main__':
    useage()





