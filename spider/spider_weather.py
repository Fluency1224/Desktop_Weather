#########################################################################
# File Name: spider_weather.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: 2018年05月04日 星期五 23时21分27秒
#########################################################################
#!/usr/bin/python3
#!coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen('http://www.weather.com.cn/weather/101190101.shtml')

soup = BeautifulSoup(resp, 'html.parser')

#第一个包含class="tem"的标签 存放的是今天天气的数据标签
tagToday = soup.find('p', class_="tem")

try:
    temperatureHigh = tagToday.span.string
except AttributeError as e:
    temperatureHigh = tagToday.find_next('p', class_="tem").span.string

temperatureLow = tagToday.i.string

weather = soup.find('p', class_="wea").string

print('最高气温：' + temperatureHigh)
print('最低气温：' + temperatureLow)
print('天气：' + weather)



