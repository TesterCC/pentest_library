#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#python灰帽编程QQ群  292041723（100人小群做过PY安全编程的进）
#IP段端口扫描

import sys
import socket
import threading,time
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import time #获取时间和延时
#----------------------------------------------------------------
def ip2num(ip):   #移位
    ip = [int(x) for x in ip.split('.')]
#    print ip
#    print ip[0]<<24
#    print ip[1]<<16
#    print ip[2]<<8
#    print ip[3]
    return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]   #<<是位移
#<<右移一个就是 * 2 意思就是 ip[0]*2^24 + ip[1]*2^16+ip[2]*2^8+ip[3]
#ipv4地址，是一个32位的二进制数，每8位转换成十进制，就是普通看到的那种形式了

def num2ip(num):
#    if num>=IPend:
#        print u"IP导入数组完成"
    return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                              (num & 0x00ff0000) >> 16,
                              (num & 0x0000ff00) >> 8,
                              num & 0x000000ff  )

def gen_ip(Aip1,Aip2):  #返回数组
#    global IPend
#    IPend=Aip2
    return [num2ip(num) for num in range(Aip1,Aip2+1) if num & 0xff]   #range(1,5) #代表从1到5(不包含5)
#----------------------------------------------------------------

if __name__=='__main__':
#    print ip2num("1.2.3.4")
#    data=16909060
#    print num2ip(data)
    list_ip=gen_ip(ip2num("192.168.2.1"),ip2num("192.168.3.254"))
    print u"需要扫描"+str(len(list_ip))+u"个IP"
    I1 = 0 #得到list的第一个元素
    while I1 < len(list_ip):
        print list_ip[I1]
        I1 = I1 + 1   #一层