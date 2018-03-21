#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#python灰帽编程QQ群  292041723（100人小群做过PY安全编程的进）
#字典的生成


def open_txt():  #打开TXT文本写入数组
    try:
        xxx = file('admin.txt', 'r')
        for xxx_line in xxx.readlines():
            passlist.append(xxx_line)
        xxx.close()
    except:
        return 0

def list_del():  #清空list列表
    try:
        i = 0 #得到list的第一个元素
        while i < len(passlist):
            del passlist[i]
            del list_passwed[i]
    except:
        return 0


def link_ftp():  #TXT导入数组    组合密码
    www="127.0.0.1"
    #passlist = list(set(passlist))   #python 列表去重
    for i in passlist:
        if i not in list_passwed:
            list_passwed.append(i)
        ######################################   遍历数组组合出 密码
    I1 = 0 #得到list的第一个元素
    while I1 < len(list_passwed):
        #print "第几组密码：",I1
        if I1==len(list_passwed):
            break  #退出循环
        I2 = 0 #得到list的第一个元素
        while I2 < len(list_passwed):
            print u"IP:",www,u"用户名:",list_passwed[I1],u"密码:",list_passwed[I2]
            I2 = I2 + 1  #二层
        I1 = I1 + 1   #一层




if __name__=='__main__':
    global  passlist  #声明全局变量
    passlist = []    #用户名：anonymous 密码为空
    global  list_passwed  #列表去重，不打乱原来的顺序
    list_passwed=[]
    ###########
    open_txt()   #TXT导入数组
    link_ftp()  #TXT导入数组    组合密码
    list_del()  #清空list列表