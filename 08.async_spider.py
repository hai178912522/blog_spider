# -*- coding: utf-8 -*-
# @Time : 2022-11-28 22:09
# @Author : ZZZZZHHHHH
# @FileName: 08.async_spider.py
# @Software: PyCharm
import asyncio
import aiohttp
import time
import blog_spider

async def async_craw(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            print(f"craw url:{url} size:{len(result)}")

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url)) for url in blog_spider.urls
]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"cost time:{end-start}")