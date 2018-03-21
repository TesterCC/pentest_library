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
    if num>=IPend:
        print u"IP导入数组完成"
    return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                              (num & 0x00ff0000) >> 16,
                              (num & 0x0000ff00) >> 8,
                              num & 0x000000ff  )

def gen_ip(Aip1,Aip2):  #返回数组
    global IPend
    IPend=Aip2
    return [num2ip(num) for num in range(Aip1,Aip2+1) if num & 0xff]   #range(1,5) #代表从1到5(不包含5)
#----------------------------------------------------------------

def socket_port(ip,PORT):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        s.connect((ip,PORT))
#        print ip,u":",PORT,u"端口开放"

        result=s.connect_ex((ip,PORT))
        if(result==0):
            print ip,u":",PORT,u"端口开放"
#        xxx = open('ip.txt','a+')  #open file
#        xxx.seek(1)
#        xxx.write(str(ip))
#        xxx.write('\n')
#        xxx.close()
        s.close()
        print ".",

        #xxx=file('ip.txt','w')
        #xxx.write(str(ip))
        #xxx.write('\n')
        #xxx.close()

    except:
        #print ip,u":",PORT,u"端口未开放"
        #print ".",
        print u"扫描端口异常2"


if __name__=='__main__':
    list_ip=gen_ip(ip2num("222.138.227.0"),ip2num("222.138.228.0"))
    print u"需要扫描"+str(len(list_ip))+u"个IP"
    I1 = 0 #得到list的第一个元素
    port=80
    while I1 < len(list_ip):
        #print list_ip[I1]
        time.sleep(0.1) #确保先运行Seeker中的方法
        thread.start_new_thread(socket_port,(list_ip[I1],port))
        I1 = I1 + 1   #一层

#http://www.cnblogs.com/hbycool/articles/2749975.html

