#!/usr/bin/env python
# encoding:utf-8

import urllib2
import lxml.html

class WoYun():
    urlList =[]   # 存url列表

    def getPage(self, url):
        pageUrl = url
        request = urllib2.Request(pageUrl)
        response = urllib2.urlopen(request)
        html = response.read()
        url = lxml.html.fromstring(html)
        result = url.xpath('//*[@*]/h3/a')
        for r in result:
            list = {'title': r.text,'url': r.get('href')}
            self.urlList.append(list)

    def getUrlList(self):
        return self.urlList

    def getContent(self, url):
        pageUrl = url
        request = urllib2.Request(pageUrl)
        response = urllib2.urlopen(request)
        html = response.read()
        url = lxml.html.fromstring(html)
        result = url.xpath(' /html/body/main/div[1]/article/section')
        text = ''
        for r in result:
            text = r.text_content()
        return text

if __name__ == '__main__':
    url = 'http://drops.wooyun.org/category/tips/page/'  # 乌云知识库技术分享分类下所有文章 ，其他分类更换此url
    w = WoYun()
    for i in range(1):
        w.getPage(url + str(i + 2))

    for key in w.getUrlList():
        print '=================' + key.get('title') + '==========================='
        print 'url : ' + key.get('url')
        print w.getContent(key.get('url'))
        print '======================================================================'
