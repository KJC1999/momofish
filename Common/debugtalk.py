"""
创建人：孔健聪
创建时间：2022.08.10
"""
# coding=utf-8
import json
import json
import re
import requests
import datetime
import sxtwl
import http.client
import hashlib
import urllib
import random
from bs4 import BeautifulSoup
from urllib import request

appid = '20220820001314146'  # 百度接口id
secretKey = 'lqlvlMm2gG1Tya3ClABn'  # 百度接口秘钥

httpClient = None
myurl = '/api/trans/vip/translate'

api_id = '20220820001314146'
key = 'lqlvlMm2gG1Tya3ClABn'

language_type = {'中文简体': 'zh',
                 '中文繁体': 'cht',
                 '英文': 'en',
                 '日文': 'jp',
                 '韩文': 'kor'}


def translate_api(content, tolang):
    salt = random.randint(32768, 65536)
    q = content
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(
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
    sign = appid + content + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.parse.quote(
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
           "Friday": '周五', "Saturday": '周六', "Sunday": '周日'}
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
    str = data.strip("[]{};,").replace(' ', '').replace(':', ',').replace('\n', '').replace('"', '')  # 做字符去除
    list = str.split(',')  # 去引号，以及根据逗号切割str从而转为list
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
        if not '\u4e00' <= list2[i] <= '\u9fa5':
            list2[i] = list2[i]
        else:
            str1 = list2[i].replace('\\n', '991128')
            print(str1)
            list2[i] = translate_api(str1, language_type[tolang]).replace('991128', '\n').replace('(', '').replace(')', '')
            print(list2[i])
    for i in range(len(list1)):
        result.update({list1[i]: list2[i]})
    return json.dumps(result, ensure_ascii=False, indent=4)


