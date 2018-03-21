#!/usr/bin/env python
# coding:utf-8

# P10-13
# simple scanner demo

import socket


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(7)
        s = socket.socket()
        banner = s.recv(1024)
        return banner
    except:
        return "Timeout."


def checkVulns(banner):
    if 'FreeFloat Ftp Server' in banner:
        print "[+] FreeFloat FTP Server is vulnerable."
    elif '3Com' in banner:
        print "[+] 3CDaemon FTP Server is vulnerable."
    elif 'Ability server' in banner:
        print "[+] Ability Server is vulnerable."
    else:
        print "[-] FTP Server is not vulnerable."
    return


def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '122.248.239.69'

    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print '[+] '+ip1+': '+banner1

    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] '+ip2+': '+banner2

    banner3 = retBanner(ip3, port)
    if banner3:
        print '[+] '+ip3+': '+banner3


if __name__ == '__main__':
    main()

