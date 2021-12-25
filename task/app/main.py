# -*- coding: utf-8 -*-

"""
@Time : 2021/3/13
@Author : Canking
@File : day_task
@Description :
"""
import json
import os
import time
import requests
from bs4 import BeautifulSoup
from flask import Flask


def get_day():
    pre = {'User-agent': 'Mozilla/5.0'}
    res = requests.get("http://120.52.185.46/shh/portal/bjjs2020/index_new.aspx", headers=pre)
    soup = BeautifulSoup(res.text, "html.parser")

    target = soup.find_all(class_='clfqytj_content_new')
    times = target[0].find_all('h3')
    time_day = times[1]
    time_day = time_day.string.replace("存量房网上签约", '')

    tables = target[0].find_all('table')
    item = tables[1]

    fieldnames = ['时间戳', '日期', '网上签约套数', '网上签约面积(㎡)', '住宅签约套数', '住宅签约面积(㎡)']
    now = int(time.time())
    row_value = {"时间戳": now, "日期": time_day}
    index = 2
    for tr in item.findAll('tr'):
        tds = tr.findAll('td')

        row_value[fieldnames[index]] = (tds[1].text)
        index = index + 1
    return row_value


app = Flask(__name__)


@app.route('/day')
def get_day_signatory():
    return json.dumps(get_day(), ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
