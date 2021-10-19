# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 08:59:28 2021

@author: Ruich
"""
import time
import math
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

PRIMES = [112272535095293] * 30000000

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return True
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n):
        if n % i == 0:
            return False
        return True

def  single_process():
    for num in PRIMES:
        is_prime(num)

def multhread_process():
    with ThreadPoolExecutor() as pool:
        result = pool.map(is_prime,PRIMES)
        

def mulprocess_process():
    with ProcessPoolExecutor() as pool:
        result = pool.map(is_prime,PRIMES)
        
if __name__ == '__main__':
    start = time.time()
    single_process()
    end = time.time()
    print("Single thread {}".format(end - start))
    
    start = time.time()
    single_process()
    end = time.time()
    print("multi thread {}".format(end - start))
    
    # in single core pc multiprocess will not be faster
    start = time.time()
    single_process()
    end = time.time()
    print("multi process {}".format(end - start))