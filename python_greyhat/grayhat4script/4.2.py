#!/usr/bin/env python
#-*- coding: UTF-8 -*-
#python灰帽编程QQ群  292041723（100人小群做过PY安全编程的进）
#字典的生成
from collections import defaultdict, deque


WEAK_USERNAME = [p.replace('\n','') for p in open('username.dic').readlines()]
WEAK_PASSWORD = [p.replace('\n','') for p in open('password.dic').readlines()]

def get_sdomain(domain):  #域名拆解www.baidu.com->baidu.com
    suffixes = 'ac', 'ad', 'ae', 'aero', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'arpa', 'as', 'asia', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'biz', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cat', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'com', 'coop', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'edu', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gov', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'info', 'int', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jobs', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mil', 'mk', 'ml', 'mm', 'mn', 'mo', 'mobi', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'name', 'nc', 'ne', 'net', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'org', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'pro', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tel', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'xn', 'ye', 'yt', 'za', 'zm', 'zw'
    sdomain = []
    bdomain = False
    for section in domain.split('.'):
        if section in suffixes:
            sdomain.append(section)
            bdomain = True
        else:
            sdomain = [section]
    return '.'.join(sdomain) if bdomain  else ''

def get_ssdomain(domain):  #域名拆解www.baidu.com->baidu
    sdomain = get_sdomain(domain)  #先解析一道
    ssdomian = sdomain.partition('.')[0] if sdomain else ''
    return ssdomian

def login(host):
    #得到sdomain和ssdomain
    domain = host   #不明白未什么还要赋值  直接使用host变量不就可以了吗
    sdomain = get_sdomain(domain)  #域名拆解www.baidu.com->baidu.com
    ssdomain = get_ssdomain(domain)  #域名拆解www.baidu.com->baidu
    #拆解不够完全有这样的一个玉米  123456.blog.baidu.com.cn   ！！！！！！！
    global accounts
    accounts = deque()   #list数组
    #准备 用户名和密码
    for username in WEAK_USERNAME:   #导入用户名#WEAK_USERNAME=username.dic
        if  '%domain%' in username or '%sdomain%' in username or '%ssdomain%' in username:
            if sdomain=='':
                continue  #跳过
            else:
                username = username.replace('%domain%',domain)  #返回根据正则表达式进行文字替换后的字符串的复制
                username = username.replace('%sdomain%',sdomain)
                username = username.replace('%ssdomain%',ssdomain)

        for password in WEAK_PASSWORD:   #导入密码#WEAK_PASSWORD=password.dic
            if '%domain%' in password or '%sdomain%' in password or '%ssdomain%' in password:
                if sdomain=='':
                    continue  #跳过
                else:
                    password = password.replace('%domain%',domain)
                    password = password.replace('%sdomain%',sdomain)
                    password = password.replace('%ssdomain%',ssdomain)

            password = password.replace('%null%','')
            password = password.replace('%username%',username)

            if (username,password) not in accounts:#list数组
                accounts.append((username,password))#添加到 list数组
                ##################################################################

if __name__=='__main__':
    login("www.baidu.com")
    print u"组合出",len(accounts),u" 次密码"
    account = None   #None=NULL  数组
    while accounts:#list数组
        if not account and accounts:#list数组
            account = accounts.pop()   #list数组  输出

        #绝对不要尝试
        if not account:   #数组无数据了就跳出
           break   #跳出

        print u"用户名：",account[0],u"密码：",account[1]
        account = None  #None=NULL


