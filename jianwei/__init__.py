import os
import time

import requests
from bs4 import BeautifulSoup
import csv

pre = {'User-agent': 'Mozilla/5.0'}
res = requests.get("http://120.52.185.46/shh/portal/bjjs2020/index_new.aspx", headers=pre)
print(res.status_code)
rep = res.text
soup = BeautifulSoup(rep, "html.parser")

# print(soup.prettify())


target = soup.find_all(class_='clfqytj_content_new')

# soup_target = target[0].children
#
# for item in  soup_target:
#     print(item)
times = target[0].find_all('h3')
time_day = times[1]
print(time_day.string)
time_day = time_day.string.replace("存量房网上签约", '')
print(time_day)

tables = target[0].find_all('table')
# monthSignatoryDataFile = open('month_net_signatory_data.csv', 'wt+')
# monthSignatoryZoneFile = open('month_net_signatory_zone.csv', 'wt+')
# monthSignatoryAgencyFile = open('month_net_signatory_agency.csv', 'wt+')

item = tables[1]

try:
    len = os.path.getsize('day_net_signatory.csv')
except:
    len = 0

with open('day_net_signatory.csv', 'a+') as csv_file:
    fieldnames = ['时间戳', '日期', '网上签约套数', '网上签约面积(㎡)', '住宅签约套数', '住宅签约面积(㎡)']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    if len < 1:
        writer.writeheader()
    print("处理new Table")
    now = int(time.time())
    row_value = {"时间戳": now, "日期": time_day}
    index = 2
    for tr in item.findAll('tr'):
        tds = tr.findAll('td')

        row_value[fieldnames[index]] = (tds[1].text)
        index = index + 1
    print(str(row_value))
    writer.writerow(row_value)

print('处理完成')
