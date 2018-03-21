#!usr/bin/python
# coding=utf-8
# python自动化测试框架selenium实现非法营销
# 因公司运营妹子要求，做的自动化运营脚本

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

username='xxxxx@qq.com' #网站账号
password='xxxxxx' #网站密码
msg=u'在吗？' #私信内容
startIndex=100
endIndex=500

browser = webdriver.Firefox()
browser.get('http://www.shougongke.com/')
browser.find_element_by_xpath('//*[@id="sgk-header"]/div/div[2]/a[1]').click()
browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[4]/input').click()
time.sleep(1)

for x in range(startIndex, endIndex):
    try:
        url='http://www.shougongke.com/user/'+str(x+1)+'.html'
        browser.get(url)
        browser.find_element_by_xpath('//*[@id="sgk-warp"]/div/div[1]/div[2]/div/a[2]').click()
        time.sleep(2)
        browser.find_element_by_id('J_wkitTextarea').send_keys(msg)
        browser.find_element_by_xpath('//*[@id="J_wkitMsgSendBtn"]').click()
        time.sleep(2)
    except Exception, e:
        print 'error'

# browser.close() #url
