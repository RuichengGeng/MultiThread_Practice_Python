# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:00:33 2021

@author: Ruich
"""

import threading
import time

lock = threading.Lock()

class Account:
    def __init__(self,balance):
        self.balance = balance
        
def draw(account,amount):
    if account.balance >= amount:
        time.sleep(0.1)
        account.balance -= amount
        print("success, balance = {}".format(account.balance))
    else:
       print("fail, balance = {}".format(account.balance))
        
def draw_lock(account,amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            account.balance -= amount
            print("success, balance = {}".format(account.balance))
        else:
           print("fail, balance = {}".format(account.balance))
       
if __name__ == '__main__':
    account = Account(800)
    
    ta = threading.Thread(name = 'a',target = draw_lock,args=(account,600))
    tb = threading.Thread(name = 'b',target = draw_lock,args=(account,600))
    
    ta.start()
    tb.start()
