# -*- coding: utf-8 -*-
# @Time : 2022-11-28 21:41
# @Author : ZZZZZHHHHH
# @FileName: 06.thread_process_cpu_bound.py
# @Software: PyCharm
import math
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

PEIMES = [112233111123123123] *1000


def is_prime(n):
    if n <2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def single_thread():
    for number in PEIMES:
        is_prime(number)

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PEIMES)

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,PEIMES)

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread", end - start)

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread", end - start)

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process", end - start)









