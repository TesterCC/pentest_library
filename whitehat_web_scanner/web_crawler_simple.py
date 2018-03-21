#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/8/25 17:12'

# 白帽子讲Web扫描 P44-45  伪代码，无法正常运行

from Queue import Queue


MAX = 100
condition = True


def get_new_url():
    pass

# Initial Web URL
root_url = "http://www.anquanbao.com"

# URL Queue
url_queue = Queue(MAX)
url_queue.put(root_url)

while True:
    # 当满足一定条件时，停止爬取
    if condition:
        break

    # 从队列中获取待爬行的URL
    current_url = url_queue.get()

    # 获取当前页面中新的URL
    new_urls = get_new_url(current_url)
    seen = []

    # 抽取新的URL放入队列中
    for next_url in new_urls:
        if next_url not in seen:
            seen.put(next_url)
            url_queue.put(next_url)
