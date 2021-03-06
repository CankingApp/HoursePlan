import os
import time

import requests
from bs4 import BeautifulSoup
import csv

_FILE_NAME_SAVE = 'day_net_signatory_pro.csv'
pre = {'User-agent': 'Mozilla/5.0'}
res = requests.get("http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=307749", headers=pre)
print(res.status_code)
rep = res.text
soup = BeautifulSoup(rep, "html.parser")

target = soup.find_all(class_='portlet')

target_table = target[1].find_all('table')

time_day = target_table[1].find_all(class_='f14a1')
time_day = time_day[1].string.replace("新发布房源", '').strip()
print(time_day)

tables = target_table[1].find_all('table')

try:
    file_len = os.path.getsize(_FILE_NAME_SAVE)
except:
    file_len = 0



def writeFile():
    has_get = False

    with open(_FILE_NAME_SAVE, 'rb+') as f:
        off = -100
        while True:
            f.seek(off, 2)
            lines = f.readlines()
            if len(lines) >= 2:
                last_line = lines[-1]
                if time_day in str(last_line):
                    has_get = True
                break
            off *= 2


    with open(_FILE_NAME_SAVE, 'a+') as csv_file:
        fieldnames = ['时间戳', '日期', '可售房源套数', '可售房源面积(m2)', '可售住宅套数', '可售住宅面积(m2)', '新发布房源套数',
                      '新发布房源面积(m2)', '新发布住宅套数', '新发布住宅面积(m2)', '网上签约套数',
                      '网上签约面积(㎡)', '住宅签约套数', '住宅签约面积(㎡)']
        if has_get:
            print("发现已获取该天数据：" + time_day)
            return None

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if file_len < 1:
            writer.writeheader()
        print("处理new Table")
        now = int(time.time())
        row_value = {"时间戳": now, "日期": time_day}
        index = 2
        for tr in tables[0].find_all('tr'):
            tds = tr.find_all('td')
            try:
                find = tds[1]
            except:
                continue
            row_value[fieldnames[index]] = (find.text.strip())
            index = index + 1

        for tr in tables[1].findAll('tr'):
            tds = tr.findAll('td')
            try:
                find = tds[1]
            except:
                continue
            row_value[fieldnames[index]] = (find.text.strip())
            index = index + 1

        for tr in tables[3].findAll('tr'):
            tds = tr.findAll('td')
            try:
                find = tds[1]
            except:
                continue
            row_value[fieldnames[index]] = (find.text.strip())
            index = index + 1
        print(str(row_value))
        writer.writerow(row_value)


writeFile()

print('处理完成')
