# -*- coding: utf-8 -*-
# @Time : 2022-11-28 20:49
# @Author : ZZZZZHHHHH
# @FileName: 03.lock_concurrent.py
# @Software: PyCharm
import threading
import time
lock = threading.Lock()

class Account:
    def __init__(self, balance):
        self.balance = balance



def draw(account, amount):
    with lock:
        if account.balance >= amount:
            print(threading.current_thread().name, "get money", amount)
            time.sleep(0.1)
            account.balance -= amount
            print(threading.current_thread().name, "left money", account.balance)
        else:
            print(threading.current_thread().name, "not enough money")

if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(name="Thread-A", target=draw, args=(account, 800))
    tb = threading.Thread(name="Thread-B", target=draw, args=(account, 800))
    ta.start()
    tb.start()