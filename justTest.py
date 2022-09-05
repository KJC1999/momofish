import base64
import json
import ssl
import requests
import random
import math
import re
from lxml import etree
from urllib import request, parse
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


def weiBo_trendingTopic():
    requests.packages.urllib3.disable_warnings()
    session = requests.session()
    session.verify = False
    session.timeout = 20
    # 定义一个hots用于存放热搜title和跳转link
    hots = []
    # 访客接口（获取tid），用该接口返回的tid拼接cookie
    tid_url = "https://passport.weibo.com/visitor/genvisitor"
    # 热搜接口
    hots_url = "https://s.weibo.com/top/summary?cate=realtimehot"
    link = "https://s.weibo.com/weibo?q=%23{}%23&Refer=top"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36"
    }
    # 请求参数必用
    data = "cb=gen_callback&fp=%7B%22os%22%3A%221%22%2C%22browser%22%3A%22Chrome80%2C0%2C3970%2C5%22%2C%22fonts%22%3A%22undefined%22%2C%22screenInfo%22%3A%221920*1080*24%22%2C%22plugins%22%3A%22Portable%20Document%20Format%3A%3Ainternal-pdf-viewer%3A%3AChrome%20PDF%20Plugin%7C%3A%3Amhjfbmdgcfjbbpaeojofohoefgiehjai%3A%3AChrome%20PDF%20Viewer%7C%3A%3Ainternal-nacl-plugin%3A%3ANative%20Client%22%7D"
    # 获取tid
    headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    tid = json.loads(session.post(url=tid_url, headers=headers, data=data).content.decode('utf-8')[36:-2])['data']['tid']
    del headers['Content-Type']
    # 获取访客cookie
    cookie_url = "https://passport.weibo.com/visitor/visitor?a=incarnate&t=" + parse.quote(
        tid) + "&w=2&c=095&gc=&cb=cross_domain&from=weibo"
    session.get(url=cookie_url.encode('utf-8'), headers=headers)
    # 发送get请求
    res = session.get(url=hots_url, headers=headers)
    # 对响应信息进行转码解析
    html = res.content.decode('utf-8', "ignore")
    soup = BeautifulSoup(html, 'html.parser')
    # 真正的热搜的 tr 标签的子标签里
    data = soup.select("tr")
    for item in data:
        try:
            if item.contents[1].contents[0].isdigit():
                title = item.contents[3].contents[1].contents[0]
                # 设置url内中文转义规则
                rules = b'/:?=%23&'
                # parse.quote进行转义，以进行链接全英文符号显示
                hots.append([parse.quote(link.format(title), rules), title])
        except:
            pass
    print(hots)
    return hots


def zhiHu_trendingTopic():
    hots = []
    url = 'https://www.zhihu.com/billboard'
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    script = json.loads(soup.find('script', id="js-initialData", type="text/json").get_text(), strict=False)
    hotsList = script['initialState']['topstory']['hotList']
    for i in range(len(hotsList)):
        hots.append([hotsList[i]['target']['link']['url'], hotsList[i]['target']['titleArea']['text']])
    print(hots)
    return hots

def CSDN_trendingTopic():
    hots = []
    headers = {
        "user-agent": "Baiduspider"
    }
    res = requests.get(f"https://blog.csdn.net/phoenix/web/blog/hotRank?page=0&pageSize=50", headers=headers)
    res.close()
    data = res.json()['data']
    for i in range(len(data)):
        hots.append([data[i]['articleDetailUrl'], data[i]['articleTitle']])
    print(hots)
    return hots


# weiBo_trendingTopic()
# zhiHu_trendingTopic()
# CSDN_trendingTopic()
