#!/usr/bin/python
#coding:utf-8

"""
Author: Andy Tian
Contact: tianjunning@126.com
Software: PyCharm
Filename: proxy.py
Time: 2018/8/6 16:33
"""
from scrapy import Spider


class ProxyIp(Spider):
    name = 'ip'
    #http://www.882667.com/
    start_urls = ['http://ip.cn']

    def parse(self, response):
        print(response.text)