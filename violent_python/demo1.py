#!/usr/bin/env python
# coding:utf-8

# P9-10

import socket


socket.setdefaulttimeout(3)
s = socket.socket()

try:
    s.connect(("www.baidu.com", 80))
    ans = s.recv(2048)
    print ans

    if ("FreeFloat Ftp Server" in ans):
        print "[+] FreeFloat FTP Server is vulnerable."
    elif ("3Com" in ans):
        print "[+] 3CDaemon FTP Server is vulnerable."
    elif ("Ability server" in ans):
        print "[+] Ability Server is vulnerable."
    else:
        print "[-] FTP Server is not vulnerable."

except Exception, e:
    print "[-] Error = "+str(e)

