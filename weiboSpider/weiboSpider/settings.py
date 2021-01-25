# -*- coding: utf-8 -*-

# Scrapy settings for weiboSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'weiboSpider'

SPIDER_MODULES = ['weiboSpider.spiders']
NEWSPIDER_MODULE = 'weiboSpider.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weiboSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.82',
    'Connection': 'keep-alive',
    'Host': 'weibo.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie':random.choice([    #购买账号建立cookiepool
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lxoYYU8q2xrxqTSKn_CpsdU9FRk9hkXgjFBd-ZFLtWgw.; SUB=_2A25NBfusDeRhGedL7FcQ9CnKzDiIHXVuCYXkrDV6PUJbktANLVGnkW1NVLlRXD1fNE5OHfzgjAj4Le2YREsDbNzK; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFc_RjAOE7eziX0B9Cxd0ZX5NHD95QpSKMfeKBNSoMXWs4Dqc_zi--fi-z7iKysi--fiKysi-8si--NiKnRi-zpi--Ri-8siK.fi--Ri-8siK.fi--fi-z7i-zpi--Ri-8siK.fi--Ri-8siK.f; SSOLoginState=1610714109'
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1ly4WN5Y7JF9S8Yt76TXvsM8hjszbiVDg2dNza4ztwPAc.; SUB=_2A25NBfpiDeRhGedG6FsZ8ijEzjiIHXVuCYYqrDV6PUJbktANLUflkW1NUUy5fomuAPwIr6k2MT8J7vvxz5wIpU_H; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Q.PBhxnseuIPdTqccfTLo5NHD95Qp1he41hzc1h-XWs4Dqcj.i--NiK.4i-i2i--4iK.ciKyFi--fiKnfiK.pi--ci-z7i-zX; SSOLoginState=1610713650'
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWzIL0bNFvHceYYZgGGQ8jF5NHD95Qp1hB4eKn4eh50Ws4Dqcj_i--fi-isiKn0i--NiKnpi-zfi--ci-zRiK.7i--fi-ihiKn7i--Ni-iWi-is; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lIOJvS_dA7JJ7cE8eypaH8Zv7HiPlgzPFf6Nx25nfyLo.; SUB=_2A25NBfjJDeRhGedG71sQ-CfMyz-IHXVuCZiBrDV6PUJbktANLWrDkW1NUT_K-AioZvOx2Q1YSXElKPwm-pL6CV19; SSOLoginState=1610713241'
#'SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lhajquDLFTFhx9kYhI3ieGWNb_H2g8ZoGI4cEzWjI7Gg.; SUB=_2A25NBSB-DeRhGeVG6FIT-CrKzTiIHXVuBkA2rDV6PUNbktANLXn2kW1NT6CtQ1TLm5kUNF4bU4YdWpMyxCCA_lsA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFXSvMYvQD3wFF8om.-PVW45JpX5KMhUgL.FoeRe05E1hBcSoB2dJLoIEBLxKqL1-eL1hnLxKnL1h.LBozLxK-LBKBLBo2LxK.L1hML12Bt; SSOLoginState=1610698798; ALF=1613290798; _T_WM=b812b70c51f3d17074fb0ffbe6892817'
])
}

COOKIESPOOL={
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lxoYYU8q2xrxqTSKn_CpsdU9FRk9hkXgjFBd-ZFLtWgw.; SUB=_2A25NBfusDeRhGedL7FcQ9CnKzDiIHXVuCYXkrDV6PUJbktANLVGnkW1NVLlRXD1fNE5OHfzgjAj4Le2YREsDbNzK; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFc_RjAOE7eziX0B9Cxd0ZX5NHD95QpSKMfeKBNSoMXWs4Dqc_zi--fi-z7iKysi--fiKysi-8si--NiKnRi-zpi--Ri-8siK.fi--Ri-8siK.fi--fi-z7i-zpi--Ri-8siK.fi--Ri-8siK.f; SSOLoginState=1610714109'
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1ly4WN5Y7JF9S8Yt76TXvsM8hjszbiVDg2dNza4ztwPAc.; SUB=_2A25NBfpiDeRhGedG6FsZ8ijEzjiIHXVuCYYqrDV6PUJbktANLUflkW1NUUy5fomuAPwIr6k2MT8J7vvxz5wIpU_H; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Q.PBhxnseuIPdTqccfTLo5NHD95Qp1he41hzc1h-XWs4Dqcj.i--NiK.4i-i2i--4iK.ciKyFi--fiKnfiK.pi--ci-z7i-zX; SSOLoginState=1610713650'
    'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWzIL0bNFvHceYYZgGGQ8jF5NHD95Qp1hB4eKn4eh50Ws4Dqcj_i--fi-isiKn0i--NiKnpi-zfi--ci-zRiK.7i--fi-ihiKn7i--Ni-iWi-is; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lIOJvS_dA7JJ7cE8eypaH8Zv7HiPlgzPFf6Nx25nfyLo.; SUB=_2A25NBfjJDeRhGedG71sQ-CfMyz-IHXVuCZiBrDV6PUJbktANLWrDkW1NUT_K-AioZvOx2Q1YSXElKPwm-pL6CV19; SSOLoginState=1610713241'
#'SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lhajquDLFTFhx9kYhI3ieGWNb_H2g8ZoGI4cEzWjI7Gg.; SUB=_2A25NBSB-DeRhGeVG6FIT-CrKzTiIHXVuBkA2rDV6PUNbktANLXn2kW1NT6CtQ1TLm5kUNF4bU4YdWpMyxCCA_lsA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFXSvMYvQD3wFF8om.-PVW45JpX5KMhUgL.FoeRe05E1hBcSoB2dJLoIEBLxKqL1-eL1hnLxKnL1h.LBozLxK-LBKBLBo2LxK.L1hML12Bt; SSOLoginState=1610698798; ALF=1613290798; _T_WM=b812b70c51f3d17074fb0ffbe6892817'
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weiboSpider.middlewares.WeibospiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'weiboSpider.middlewares.WeibospiderDownloaderMiddleware': 543,
    'weiboSpider.middlewares.RandomUserAgentMiddleware':1,  #访问优先
    'weiboSpider.middlewares.ProxyMiddleware':555,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'weiboSpider.pipelines.WeibospiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXY_URL = 'http://localhost:5555/random'
RETRY_HTTP_CODES = [302, 401, 403, 408, 414, 500, 502, 503, 504]    #报错码