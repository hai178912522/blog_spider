# -*- coding: utf-8 -*-
# @Time : 2022-11-28 21:53
# @Author : ZZZZZHHHHH
# @FileName: 07.flask_process_pool.py
# @Software: PyCharm
import flask
import time
from concurrent.futures import ProcessPoolExecutor
import math
import json


app = flask.Flask(__name__)

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

@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    result = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, result)))

if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()
    app.run()



