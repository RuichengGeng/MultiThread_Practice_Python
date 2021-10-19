# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:25:11 2021

@author: Ruich
"""
import threading
import requests
import time

def craw(url):
    r = requests.get(url)
    print(url,len(r.text))
    
def single_thread_craw(urls):
    print("Single thread start")
    for url in urls:
        craw(url)

def multi_thread_craw(urls):
    print("multi thread start")
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target = craw,args=(url,))
            )
        
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
if __name__ == '__main__':
    urls = [
        f"https://www.cnblogs.com/#p{page}"
        for page in range(1,51)
        ]
    start = time.time()
    single_thread_craw(urls)
    end = time.time()
    print("Single thread {}".format(end - start))
    
    start = time.time()
    multi_thread_craw(urls)
    end = time.time()
    print("multi thread {}".format(end - start))