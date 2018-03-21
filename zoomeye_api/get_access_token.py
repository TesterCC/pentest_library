# coding: utf-8

# 很精炼，建议重点学习

import requests
import json

access_token = ''
ip_list = []

def login():
    """
        输入用户米密码 进行登录操作
    :return: 访问口令 access_token
    """
    # 如果不想手动输入，可以改造为直接传递，这样其实实现更简单
    # user = raw_input('[-] input : username :')
    # passwd = raw_input('[-] input : password :')
    user = 't...x@foxmail.com'
    passwd = '-T..'  #  need change to right
    data = {
        'username': user,
        'password': passwd
    }

    data_encoded = json.dumps(data)  # dumps 将 python 对象转换成 json 字符串

    try:
        r = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded)
        r_decoded = json.loads(r.text) # loads() 将 json 字符串转换成 python 对象  -- dict
        global access_token
        access_token = r_decoded['access_token']
        print 'Your Zoomeye API access token is:\n%s'% access_token
    except Exception,e:
        print '[-] info : username or password is wrong, please try again '
        exit()

if __name__ == '__main__':
    login()