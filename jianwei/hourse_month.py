import os
import time
from typing import List, Dict

import requests
from bs4 import BeautifulSoup
import csv

# monthSignatoryDataFile = open('month_net_signatory_data.csv', 'wt+')
# monthSignatoryZoneFile = open('month_net_signatory_zone.csv', 'wt+')
# monthSignatoryAgencyFile = open('month_net_signatory_agency.csv', 'wt+')-*

_FILE_MONTH_AGENCY_NAME_SAVE = 'month_net_signatory_agency.csv'
_FILE_MONTH_ZONE_NAME_SAVE = 'month_net_signatory_zone.csv'

pre = {'User-agent': 'Mozilla/5.0'}
res = requests.get("http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=307749", headers=pre)
print(res.status_code)
rep = res.text
soup = BeautifulSoup(rep, "html.parser")

target = soup.find_all(class_='portlet')

target_table = target[2].find_all('table')

time_day = target_table[1].find_all('td')
time_day = time_day[5].text.replace("统计结果)", '').replace("(", '').strip()
print("time:" + time_day)

try:
    len = os.path.getsize(_FILE_MONTH_AGENCY_NAME_SAVE)
except:
    len = 0

with open(_FILE_MONTH_AGENCY_NAME_SAVE, 'a+') as csv_file:
    fieldnames = ['时间戳', '日期', '房地产中介', '发布房源', '签约', '退房']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if len < 1:
        writer.writeheader()
    print("处理new Table")
    now = int(time.time())
    row_value = {"时间戳": now, "日期": time_day}
    index = 2
    agent_table = target_table[2].find_all('table')
    for tr in agent_table[0].find_all('tr'):
        tds = tr.find_all('td')
        try:
            find = tds[1]
            if '名称' in find.string:
                continue
        except:
            continue
        row_value[fieldnames[2]] = (find.text.strip())
        row_value[fieldnames[3]] = (tds[2].text.strip())
        row_value[fieldnames[4]] = (tds[3].text.strip())
        row_value[fieldnames[5]] = (tds[4].text.strip())
        writer.writerow(row_value)

    for tr in agent_table[1].find_all('tr'):
        tds = tr.find_all('td')
        try:
            find = tds[1]
            if '名称' in find.string:
                continue
        except:
            continue
        row_value[fieldnames[2]] = (find.text.strip())
        row_value[fieldnames[3]] = (tds[2].text.strip())
        row_value[fieldnames[4]] = (tds[3].text.strip())
        row_value[fieldnames[5]] = (tds[4].text.strip())
        writer.writerow(row_value)

try:
    len = os.path.getsize(_FILE_MONTH_ZONE_NAME_SAVE)
except:
    len = 0

with open(_FILE_MONTH_ZONE_NAME_SAVE, 'a+') as csv_file:
    fieldnames = ['时间戳', '日期', '区域', '套数', '成交面积']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if len < 1:
        writer.writeheader()
    now = int(time.time())
    index = 2
    zone_table = soup.find_all('table', id='table_clf2')

    target_table = zone_table[0].find_all('table')
    tmp_list: List[Dict[str, int]] = []

    for tr in target_table[0].find_all('tr'):
        tds = tr.find_all('td', recursive=False)
        try:
            find = tds[0].text
        except:
            continue
        if '县' in find:
            tmp_list.clear()
            for td in tds:
                if '县' in td.text:
                    continue
                row_value = {"时间戳": now, "日期": time_day}
                row_value[fieldnames[2]] = td.text.strip().replace('\u3000', '')
                tmp_list.append(row_value)
        elif '套' in find:
            index = 0

            for td in tds:
                if '套' in td.text:
                    continue
                row_value = tmp_list[index]
                row_value[fieldnames[3]] = (td.text.strip())
                index = index + 1

        elif '面积' in find:
            index = 0

            for td in tds:
                if '面积' in td.text:
                    continue
                row_value = tmp_list[index]
                row_value[fieldnames[4]] = (td.text.strip())
                index = index + 1
            for i in tmp_list:
                writer.writerow(i)


print('处理完成')
