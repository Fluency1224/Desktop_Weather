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

def url_soup():
    url = 'http://www.weather.com.cn/weather/101190101.shtml'
    resp = urlopen(url)
    
    soup = BeautifulSoup(resp, 'html.parser')
    return soup

#天气    
def get_weather():
    soup = url_soup()
    #第一个包含class="tem"的标签 存放的是今天天气的数据标签
    tagToday = soup.find('p', class_="tem")
    weather = soup.find('p', class_="wea").string
    return weather
#最高温
def get_temperatureHigh():
    soup = url_soup()
    #第一个包含class="tem"的标签 存放的是今天天气的数据标签
    tagToday = soup.find('p', class_="tem")
    try:
        temperatureHigh = tagToday.span.string
    except AttributeError as e:
        temperatureHigh = tagToday.find_next('p', class_="tem").span.string    
    return temperatureHigh
#最低温
def get_temperatureLow():
    soup = url_soup()
    #第一个包含class="tem"的标签 存放的是今天天气的数据标签
    tagToday = soup.find('p', class_="tem")   
    temperatureLow = tagToday.i.string    
    return temperatureLow

#风力
def get_winf():  
    soup = url_soup()
    winf = soup.find('p', class_="win").i.string  
    return winf
#紫外线指数
def get_ziwai():
    soup = url_soup()
    soup.find('li', class_="li1").em.string
    index = soup.find('li', class_="li1").span.string
    suggest = soup.find('li', class_="li1").p.string
    
    return index, suggest
#穿衣指数
def get_chuanyi():
    soup = url_soup()
    soup.find('li', class_="li3").em.string
    index = soup.find('li', class_="li3").span.string
    suggest = soup.find('li', class_="li3").p.string
    
    return index, suggest
#洗车指数
def get_cleancar():
    soup = url_soup()
    soup.find('li', class_="li4").em.string
    index = soup.find('li', class_="li4").span.string
    suggest = soup.find('li', class_="li4").p.string
    
    return index, suggest
#血糖指数
def get_xuetang():
    soup = url_soup()
    soup.find('li', class_="li5").em.string
    index = soup.find('li', class_="li5").span.string
    suggest = soup.find('li', class_="li5").p.string
    
    return index, suggest
#空气污染扩散指数
def get_air():
    soup = url_soup()
    soup.find('li', class_="li6").em.string
    index = soup.find('li', class_="li6").span.string
    suggest = soup.find('li', class_="li6").p.string
    
    return index, suggest
