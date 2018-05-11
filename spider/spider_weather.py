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

def get_weather(url):
    resp = urlopen(url)
    
    soup = BeautifulSoup(resp, 'html.parser')

    print(soup.find('p', class_="win").i.string)
    #第一个包含class="tem"的标签 存放的是今天天气的数据标签
    tagToday = soup.find('p', class_="tem")
    try:
        temperatureHigh = tagToday.span.string
    except AttributeError as e:
        temperatureHigh = tagToday.find_next('p', class_="tem").span.string    
    temperatureLow = tagToday.i.string    
    weather = soup.find('p', class_="wea").string
    
    #紫外线指数
    print(soup.find('li', class_="li1").em.string)
    print(soup.find('li', class_="li1").span.string)
    print(soup.find('li', class_="li1").p.string)
    #穿衣指数
    print(soup.find('li', class_="li3").em.string)
    print(soup.find('li', class_="li3").span.string)
    print(soup.find('li', class_="li3").p.string)
    #洗车指数
    print(soup.find('li', class_="li4").em.string)
    print(soup.find('li', class_="li4").span.string)
    print(soup.find('li', class_="li4").p.string)
    #血糖指数
    print(soup.find('li', class_="li5").em.string)
    print(soup.find('li', class_="li5").span.string)
    print(soup.find('li', class_="li5").p.string)
    #空气污染扩散指数
    print(soup.find('li', class_="li6").em.string)
    print(soup.find('li', class_="li6").span.string)
    print(soup.find('li', class_="li6").p.string)
    
    return temperatureHigh, temperatureLow, weather

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101190101.shtml'
    l1, l2, l3 = get_weather(url)
    print(l1, l2, l3)
