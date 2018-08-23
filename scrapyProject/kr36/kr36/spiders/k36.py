# -*- coding: utf-8 -*-
import json
import scrapy
from kr36.items import Kr36Item

class K36Spider(scrapy.Spider):
    name = 'k36'
    allowed_domains = ['rong.36kr.com']
    start_urls = ['https://rong.36kr.com/n/api/column/0/company?sortField=HOT_SCORE&p={}'.format(i) for i in range(1,4)]

    def parse(self, response):
        cookie = 'MEIQIA_EXTRA_TRACK_ID=18PJsogSUc3PXQLvRDNJhonafDz; kr_stat_uuid=2JHF525560312; Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3=1533529361,1533563876,1533610306; download_animation=1; _kr_p_se=e6ed3c9c-697e-4d06-90ab-232fdab71ce0; krid_user_id=795265485; krid_user_version=2; kr_plus_id=795265485; kr_plus_token=3FGFSyBzjfAW5snU84nanuLptZSmk421_239____; acw_tc=AQAAAK7vgHi7oQgAJYUmauKKwAGhI5sj; kr_plus_utype=0; MEIQIA_VISIT_ID=18TJ6MVWXLGOHSSkHK46zCRtu9f; Z-XSRF-TOKEN=eyJpdiI6IkZhcVdcL0taSTc5YkEzcUJYeUFBMXNBPT0iLCJ2YWx1ZSI6Ik5hUkZIUWF3b0lRYXlsVHp2cnN1SXpUVTV5QlFpR1VNQVBLZ3RjQ3ljSDJIamdIbE9ib3NPbEJ3WnJTbkNpVzc2SnJwWERDb3o1OHJFdVVPemg2NjZ3PT0iLCJtYWMiOiI2NmI1MTIwOWNkYTEzOWZhMWJkMzJlNWFiMWJmNWY4MzgxY2JiM2RiZWMzMTYwY2MzMjdiNDcwY2VmNzIwOGEyIn0%3D; krchoasss=eyJpdiI6IjRaTHlCUW1hTEE3WU11R2FheTlXZ0E9PSIsInZhbHVlIjoiMEVLTGFHWm94NE5DMmFHR0NoY21tb0dya0I1aTF6R0pMeDdLNVlsbWU2cWpwM09sdUVjdkN2Zmt0VVlUWE1ITzJGNkRUd1F3bVVTYnBmMjJqZ1hTSVE9PSIsIm1hYyI6IjgxMWQ4MmM1OTQ0ZjIyM2U4YTA5ZTdlYWUxODI4NGMxNmQ5ZTA2OWM5ZjYxOTM0ZmUxZWE0NjUyZDA2Y2NlNjIifQ%3D%3D'
        companyList = json.loads(response.text)['data']['pageData']['data']
        item = Kr36Item()
        #通过遍历可以获取到公司的初级信息,并且拿到公司的id做下一级的访问
        for company in companyList:
            #公司ID
            cid = company['id']
            #公司所在省市
            item['cityStr'] = company.get('cityStr','')
            #公司简要
            item['brief'] = company.get('brief','')
            #融资轮次
            item['phase'] = company.get('phase','None')
            #所属行业
            item['industryStr'] = company['industryStr']
            yield scrapy.Request(url='https://rong.36kr.com/n/api/company/{}'.format(cid),callback=self.detialParse,cookies=cookie,meta={
                'cid':cid,'item':dict(item),'cookie':cookie
            })

    def detialParse(self,response):
        cid = response.meta['cid']
        item01 = response.meta['item']
        cookie = response.meta['cookie']
        item = Kr36Item()
        detials = json.loads(response.text)['data']
        #规模
        item['scale'] = detials.get('scale','None')
        #介绍
        item['intro'] = detials.get('intro','None')
        #网站
        item['website'] = detials.get('website','None')
        #全称
        item['fullname'] = detials.get('fullName','None')
        #融资金额'
        item['fundsAmount'] = detials.get('projectStatHeader','None').get('fundsAmount','None')
        yield scrapy.Request(
            url='https://rong.36kr.com/n/api/company/{}/business-info'.format(cid),
            callback=self.bussinessInfoParse,
            cookies=cookie,
            meta={
            'item02':dict(item),'item01':item01
        })

    def bussinessInfoParse(self,response):
        # 通过返回code确定是否有详细的工商信息,code=0,表示可以获取到具体信息,code=1,标识没有具体信息
        item = Kr36Item()
        item01 = response.meta['item01']
        item02 = response.meta['item02']
        #规模
        item['scale'] = item02['scale']
        #介绍
        item['intro'] = item02['intro']
        #网站
        item['website'] = item02['website']
        #全称
        item['fullname'] = item02['fullname']
        #融资金额
        item['fundsAmount'] = item02['fundsAmount']
        # 公司所在省市
        item['cityStr'] = item01['cityStr']
        # 公司简要
        item['brief'] = item01['brief']
        # 融资轮次
        item['phase'] = item01['phase']
        # 所属行业
        item['industryStr'] = item01['industryStr']
        infos = json.loads(response.text)
        if infos['code'] == 0:
            #法人
            item['operName'] = infos['data']['basicInfo']['operName']
            #注册资金
            item['registCapi'] = infos['data']['basicInfo']['registCapi']
            #注册时间
            item['startDate']=infos['data']['basicInfo']['startDate']
            #股东
            partners =[]
            for p in infos['data']['partners']:
                partners.append(p['name'])
            item['partners'] = ','.join(partners)
            yield item
