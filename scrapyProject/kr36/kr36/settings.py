# -*- coding: utf-8 -*-

# Scrapy settings for kr36 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'kr36'

SPIDER_MODULES = ['kr36.spiders']
NEWSPIDER_MODULE = 'kr36.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 20
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1660.400',
  'Cookie':'MEIQIA_EXTRA_TRACK_ID=18PJsogSUc3PXQLvRDNJhonafDz; kr_stat_uuid=2JHF525560312; Hm_lvt_e8ec47088ed7458ec32cde3617b23ee3=1533529361,1533563876,1533610306; download_animation=1; _kr_p_se=e6ed3c9c-697e-4d06-90ab-232fdab71ce0; krid_user_id=795265485; krid_user_version=2; kr_plus_id=795265485; kr_plus_token=3FGFSyBzjfAW5snU84nanuLptZSmk421_239____; acw_tc=AQAAAK7vgHi7oQgAJYUmauKKwAGhI5sj; kr_plus_utype=0; MEIQIA_VISIT_ID=18TJ6MVWXLGOHSSkHK46zCRtu9f; Z-XSRF-TOKEN=eyJpdiI6IkZhcVdcL0taSTc5YkEzcUJYeUFBMXNBPT0iLCJ2YWx1ZSI6Ik5hUkZIUWF3b0lRYXlsVHp2cnN1SXpUVTV5QlFpR1VNQVBLZ3RjQ3ljSDJIamdIbE9ib3NPbEJ3WnJTbkNpVzc2SnJwWERDb3o1OHJFdVVPemg2NjZ3PT0iLCJtYWMiOiI2NmI1MTIwOWNkYTEzOWZhMWJkMzJlNWFiMWJmNWY4MzgxY2JiM2RiZWMzMTYwY2MzMjdiNDcwY2VmNzIwOGEyIn0%3D; krchoasss=eyJpdiI6IjRaTHlCUW1hTEE3WU11R2FheTlXZ0E9PSIsInZhbHVlIjoiMEVLTGFHWm94NE5DMmFHR0NoY21tb0dya0I1aTF6R0pMeDdLNVlsbWU2cWpwM09sdUVjdkN2Zmt0VVlUWE1ITzJGNkRUd1F3bVVTYnBmMjJqZ1hTSVE9PSIsIm1hYyI6IjgxMWQ4MmM1OTQ0ZjIyM2U4YTA5ZTdlYWUxODI4NGMxNmQ5ZTA2OWM5ZjYxOTM0ZmUxZWE0NjUyZDA2Y2NlNjIifQ%3D%3D'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'kr36.middlewares.Kr36SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'kr36.middlewares.Kr36DownloaderMiddleware': 543,
   #'kr36.proxyMidde.ProxyMidde':100
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapyProject.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
  # 'kr36.pipelines.Kr36Pipeline': 300,
   'kr36.pipelines.MongoDdPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapyProject.extensions.httpcache.FilesystemCacheStorage'

PROXIES=[
  #   {"ip":"115.223.200.30:9000"},
  #   {"ip":"119.5.1.27:1133"},
  # {'ip':'115.223.248.183:9000'},
    {"IP":"122.190.231.26:23499"}
]