# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:21:10 2021

@author: Ruich
"""
import queue
import threading
import requests
from bs4 import BeautifulSoup
import time
import random

def craw(url):
    r = requests.get(url)
    return r.text

def parse(html):
    # class "post-item-title"
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all("a",class_="post-item-title")
    return [(link["href"],link.get_text()) for link in links]

def  do_craw(url_queue:queue.Queue,html_queue:queue.Queue):
    # produce 
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        print(threading.current_thread().name,"Craw {}, url_queue size {}".format(url,url_queue.qsize()))
        time.sleep(random.randint(1,2))
    

def do_parse(html_queue:queue.Queue,fout):
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name,"result {}, url_queue size {}".format(len(result),html_queue.qsize()))
        time.sleep(random.randint(1,2))


if __name__ == '__main__':
    urls = [
        f"https://www.cnblogs.com/#p{page}"
        for page in range(1,51)
        ]
    
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)
        
    for i in range(3):
        t = threading.Thread(target=do_craw,args=(url_queue,html_queue),name = "Craw{}".format(i))
        t.start()
        
    fout = open(r'C:\Users\Ruich\Desktop\Recent\PythonPractice\mutiThread\bilibili\Craw_ProdConsume.txt',"w")
    for i in range(2):
        t = threading.Thread(target=do_parse,args=(html_queue,fout),name = "parse{}".format(i))
        t.start()
    t.join()
    fout.close()