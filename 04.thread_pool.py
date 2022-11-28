# -*- coding: utf-8 -*-
# @Time : 2022-11-28 21:08
# @Author : ZZZZZHHHHH
# @FileName: 04.thread_pool.py
# @Software: PyCharm
import concurrent.futures
import blog_spider
# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url,html in htmls:
        print(url, len(html))

print("craw done")
# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url,html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():
    #     results = future.result()
    #     print(url, results)
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        results = future.result()
        print(url, results)