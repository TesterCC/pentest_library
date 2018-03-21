#!/usr/bin/env python
# coding:utf-8

# Violent Python P13

# for x in range(1,255):
#     print "192.168.95."+str(x)
#
# portList = [21, 22, 25, 80, 110]
# for port in portList:
#     print port

portList = [21, 22, 25, 80, 110, 443, 3389]

for x in range(1,255):
    for port in portList:
        print "[+] Checking 192.168.95."+str(x)+":"+str(port)