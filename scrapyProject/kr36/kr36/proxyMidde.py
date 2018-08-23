#!/usr/bin/python
#coding:utf-8

"""
Author: Andy Tian
Contact: tianjunning@126.com
Software: PyCharm
Filename: proxyMidde.py
Time: 2018/8/6 16:35
"""
import random

from kr36.settings import PROXIES


class ProxyMidde(object):
    def process_request(self, request, spider):
            proxy = random.choice(PROXIES)
            request.meta['proxy']='http://'+proxy['IP']