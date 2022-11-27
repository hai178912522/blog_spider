# -*- coding: utf-8 -*-
# @Time : 2022-11-28 0:07
# @Author : ZZZZZHHHHH
# @FileName: 02.prodecer_consumer_spider.py
# @Software: PyCharm
import queue
import blog_spider
import time
import random
import threading


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url} ",
              "url_queue.size:", url_queue.qsize())
        time.sleep(random.randint(1, 3))

def do_parse(html_queue:queue.Queue,fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"results.size {len(results)} ",
                "html_queue.size:", html_queue.qsize())
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"Thread-Craw-{idx}")
        t.start()
    fout = open("results.txt", "w",encoding="utf-8")
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue,fout),
                                name=f"Thread-Parse-{idx}")
        t.start()


