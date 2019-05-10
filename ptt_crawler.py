import re
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import pandas as pd

def open_ptt_url(url):
    r = Request(url)
    r.add_header("user-agent", "Mozilla/5.0")
    response = urlopen(r)
    html = BeautifulSoup(response,'html.parser')
    return  html


u = input("輸入ptt文章網址：")

html=open_ptt_url(u)
main_content = html.find(id="main-content")
title = main_content.find_all('span', class_ = "article-meta-tag")
content = main_content.find_all('span', class_ = "article-meta-value")





for title,content in zip(title,content):
	'''印出標題、作者、日期、看板'''
	print(title.get_text(),":",content.get_text())
	
'''印出內文，ptt內文沒有標籤屬性，需找出文章特性'''
filtered = [ v for v in main_content.stripped_strings]
inner = ' '.join(filtered)
inner = re.sub(r'(\s)+', '', inner )
number_start = inner.index(u'間')
number_end = inner.index(u'※')
print("內文：")
print(inner[number_start+21 : number_end-2])




	

