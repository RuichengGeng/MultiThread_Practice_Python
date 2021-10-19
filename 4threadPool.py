# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:18:44 2021

@author: Ruich
"""

import threading
from concurrent.futures import ThreadPoolExecutor,as_completed
from bs4 import BeautifulSoup
import requests

def craw(url):
    r = requests.get(url)
    return r.text

def parse(html):
    # class "post-item-title"
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all("a",class_="post-item-title")
    return [(link["href"],link.get_text()) for link in links]

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1,51)
        ]

## map method


with ThreadPoolExecutor() as pool:
    htmls = pool.map(craw,urls)
    htmls = list(zip(urls,htmls))
    for url,html in htmls:
        print(url,len(html))
    
with ThreadPoolExecutor() as pool:
    futures = {}
    for url,html in htmls:
        future = pool.submit(parse,html)
        futures[future] = url
    
    ##in order parse
    # for future,url in futures.items():
    #     print(url,future.result())
        
    ##
    for future in as_completed(futures):
        url = futures[future]
        print(url,future.result())
        
    
    