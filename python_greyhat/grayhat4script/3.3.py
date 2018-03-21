#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#python灰帽编程QQ群  292041723（100人小群做过PY安全编程的进）
#IP段端口扫描

import sys
import socket
import threading,time
from threading import Thread
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import time #获取时间和延时

#----------------------------------------------------------------
class socket_port(threading.Thread):
    def __init__(self,data1,data2):
        threading.Thread.__init__(self)
        self.ip1=data1
        self.ip2=data2

    def run(self):
        list_ip=self.gen_ip(self.ip2num(self.ip1),self.ip2num(self.ip2))
        print u"需要扫描"+str(len(list_ip))+u"个IP"
        I1 = 0 #得到list的第一个元素
        port=80
        while I1 < len(list_ip):
            #print list_ip[I1]
            time.sleep(0.1) #确保先运行Seeker中的方法
            thread.start_new_thread(self.IP_port,(list_ip[I1],port))
            I1 = I1 + 1   #一层

    def IP_port(self,ip,PORT):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=s.connect_ex((ip,PORT))
            if(result==0):
                print ip,u":",PORT,u"端口开放"
                xxx = open('ip.txt','a+')  #open file
                xxx.seek(1)
                xxx.write(str(ip))
                xxx.write('\n')
                xxx.close()
            s.close()
            print ".",
        except:
            print u"扫描端口异常2"



    def ip2num(self,ip):   #移位
        ip = [int(x) for x in ip.split('.')]
    #    print ip
    #    print ip[0]<<24
    #    print ip[1]<<16
    #    print ip[2]<<8
    #    print ip[3]
        return ip[0]<<24 | ip[1]<<16 | ip[2]<<8 | ip[3]   #<<是位移
#<<右移一个就是 * 2 意思就是 ip[0]*2^24 + ip[1]*2^16+ip[2]*2^8+ip[3]
#ipv4地址，是一个32位的二进制数，每8位转换成十进制，就是普通看到的那种形式了

    def num2ip(self,num):
        if num>=IPend:
            print u"IP导入数组完成"
        return '%s.%s.%s.%s' % (  (num & 0xff000000) >> 24,
                                  (num & 0x00ff0000) >> 16,
                                  (num & 0x0000ff00) >> 8,
                                  num & 0x000000ff  )

    def gen_ip(self,Aip1,Aip2):  #返回数组
        global IPend
        IPend=Aip2
        return [self.num2ip(num) for num in range(Aip1,Aip2+1) if num & 0xff]   #range(1,5) #代表从1到5(不包含5)
    #----------------------------------------------------------------
if __name__=='__main__':
    data1="182.118.14.0"
    data2="182.118.16.0"
    socketA=socket_port(data1,data2)
    socketA.start()