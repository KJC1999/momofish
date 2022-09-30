"""
创建人：KinChung
创建时间：2022.08.10
"""
# coding=utf-8
import json
import base64
import datetime
import sxtwl
import http.client
import hashlib
import urllib
import random
import requests
import ssl
from bs4 import BeautifulSoup
from urllib import request, parse
# from paddleocr import PaddleOCR

# 百度AI平台应用id及密钥
tran_appid = '20220820001314146'  # 百度翻译id
tran_secretKey = 'lqlvlMm2gG1Tya3ClABn'  # 百度翻译密钥
# 暂时用不到了，改成本地识别。paddleocr牛逼！
ocr_appid = 'BKFVKZyxGL3lDF37B8mug1x1'  # 百度文字识别id
ocr_secretKey = 'Yq4OhwCry8ZKbvaz0t3tZDLYt0Y9wGNG'  # 百度文字识别密钥


httpClient = None
# urllib库必须要
ssl._create_default_https_context = ssl._create_unverified_context
language_type = {'中文简体': 'zh',
                 '中文繁体': 'cht',
                 '英文': 'en',
                 '日文': 'jp',
                 '韩文': 'kor'}


def ocr_api(filePath):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open(filePath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    # 先调取鉴权token
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=BKFVKZyxGL3lDF37B8mug1x1&client_secret=Yq4OhwCry8ZKbvaz0t3tZDLYt0Y9wGNG'
    access_token = requests.get(host).json()['access_token']
    # 调取百度OCR接口
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers).json()
    result = response['words_result']
    return result


# def local_ocr(filePath, lang):
#     """
#     本地调用PaddleOCR服务
#     """
#     # 用ocr_result存放结果并return
#     ocr_result = []
#     # 本地ocr需要传两个参数：lang和filePath
#     ocr = PaddleOCR(use_angle_cls=True, lang=lang)  # need to run only once to download and load model into memory
#     result = ocr.ocr(filePath, cls=True)
#     for line in result:
#         ocr_result.append(line[1][0])
#     return ocr_result


def translate_api(content, tolang):
    salt = random.randint(32768, 65536)
    q = content
    sign = tran_appid + q + str(salt) + tran_secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + tran_appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + 'auto' + '&to=' + tolang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8").replace('991128', '\\n')
        result = json.loads(result_all)

        return result['trans_result'][0]['dst']
    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()


def translate_api_custom(content, tolang):
    salt = random.randint(32768, 65536)
    sign = tran_appid + content + str(salt) + tran_secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    print(language_type[tolang])
    myurl = '/api/trans/vip/translate' + '?appid=' + tran_appid + '&q=' + urllib.parse.quote(
        content) + '&from=' + 'auto' + '&to=' + tolang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        print(result['trans_result'][0]['dst'])
        return result['trans_result'][0]['dst']
    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()


def get_weather(city):
    # 城市码
    city_codes = {'蓬江': '101281107',
                  '香洲': '101280704',
                  '端州': '101280904',
                  '宝安': '101280605'}
    if len(city) == 0:
        city = '香洲'
    url = 'http://www.weather.com.cn/weather1d/' + city_codes[city] + '.shtml'
    req = request.urlopen(url)
    html = req.read().decode('utf-8')
    weather = {}
    soup = BeautifulSoup(html, 'lxml')
    # 解析html文件
    weather['day_wea'] = soup.select('div.t > ul.clearfix > li > p.wea')[0].text
    weather['night_wea'] = soup.select('div.t > ul.clearfix > li > p.wea')[1].text
    weather['day_tem'] = soup.select('div.t > ul.clearfix > li > p.tem > span')[0].text
    weather['night_tem'] = soup.select('div.t > ul.clearfix > li > p.tem > span')[1].text
    return weather


def momofish_week(week):
    """
    根据传入的week进行相应的中文返回
    :param week:
    :return:
    """
    day = {"Monday": '周一', "Tuesday": '周二',
           "Wednesday": '周三', "Thursday": '周四',
           "Friday": '周五', "Saturday": '周六', "Sunday": '周日',
           "星期一": '周一', "星期二": '周二',
           "星期三": '周三', "星期四": '周四',
           "星期五": '周五', "星期六": '周六', "星期天": '周日'
           }
    return day[week]


def momofish_declaration():
    # 节日名 日期 是否农历
    Holidays = [["元旦", [1, 1], 0], ["春节", [1, 1], 1], ["清明节", [4, 5], 0], ["劳动节", [5, 1], 0],
                ["端午节", [5, 5], 1], ["中秋节", [8, 15], 1], ["国庆节", [10, 1], 0]]
    # 节假日字典
    Eday = {}
    # 节假日名称
    Holidays_name = []
    # 获取今天的日期与年份
    today = datetime.date.today()
    year = today.year
    text_print = []
    text = ''
    for D in Holidays:
        # 存放今年以及明年的节日
        days = [[], []]
        # 判断是否农历
        if D[2]:
            Lunarday = sxtwl.fromLunar(year, D[1][0], D[1][1])
            Lunarday2 = sxtwl.fromLunar(year + 1, D[1][0], D[1][1])
            data_today = datetime.date(Lunarday.getSolarYear(), Lunarday.getSolarMonth(), Lunarday.getSolarDay())
            data_today2 = datetime.date(Lunarday2.getSolarYear(), Lunarday2.getSolarMonth(), Lunarday2.getSolarDay())
            days[0] = (data_today - today).days
            days[1] = (data_today2 - today).days
        else:
            data_today = datetime.date(year, D[1][0], D[1][1])
            data_today2 = datetime.date(year + 1, D[1][0], D[1][1])
            days[0] = (data_today - today).days
            days[1] = (data_today2 - today).days
        for d in days:
            if 0 < d < 190:
                Holidays_name.append(D[0])
                Eday[D[0]] = d

    for n in Holidays_name:
        text_print.append("离%s还有%s天\n" % (n, Eday[n]))
    text_change = str(text_print).strip('[]').replace("'", "").replace(',', '').replace(' ', '').split('\\n')
    for i in range(0, len(text_change)):
        text += text_change[i] + '\n'
    return text


def translate_custom(data, tolang):
    list1 = []
    list2 = []
    result = {}
    a = 0
    b = 1
    str = data.strip("[]{};,").replace(' ', '').replace(':', ',').replace('\n', '').replace('"', '')  # 做相应字符去除
    list = str.split(',')  # 根据逗号切割str从而转为list
    print(list)
    # 更新单数索引
    for i in range(int(len(list) / 2)):
        list1.append(list[a])
        a += 2
    # 更新双数索引
    for i in range(int(len(list) / 2)):
        list2.append(list[b])
        b += 2
    # 判断并进行翻译转换
    for i in range(len(list2)):
        str1 = list2[i].replace('\\n', '991128')
        print(str1)
        list2[i] = translate_api(str1, language_type[tolang]).replace('991128', '\n').replace('(', '').replace(')', '')
        print(list2[i])
    for i in range(len(list1)):
        result.update({list1[i]: list2[i]})
    return json.dumps(result, ensure_ascii=False, indent=4)


def zhiHu_trendingTopic():
    hots = []
    url = 'https://www.zhihu.com/billboard'
    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # 解析知乎最底下的那层json
    script = json.loads(soup.find('script', id="js-initialData", type="text/json").get_text(), strict=False)
    hotsList = script['initialState']['topstory']['hotList']
    for i in range(len(hotsList)):
        hots.append([hotsList[i]['target']['link']['url'], hotsList[i]['target']['titleArea']['text']])
    return hots


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
    # print(hots)
    return hots


def CSDN_trendingTopic():
    hots = []
    headers = {
        "user-agent": "Baiduspider"
    }
    res = requests.get(f"https://blog.csdn.net/phoenix/web/blog/hotRank?page=0&pageSize=50", headers=headers, verify=False)
    data = res.json()['data']
    for i in range(len(data)):
        hots.append([data[i]['articleDetailUrl'], data[i]['articleTitle']])
    # print(hots)
    return hots