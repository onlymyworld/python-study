# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

from bs4 import BeautifulSoup
import requests
import csv



url2 = 'http://localhost:63342/DDIC/scr/finance/Aggregate_External_Billing.htm?_ijt=na7049ntr82qno1l473sfr9354d'
links = []
for n in range(2, 40):
    # 页面总数为39页，需要自己先从网页判断，也可以从页面抓取，后续可以完善
    link = url2 + str(n)
    links.append(link)
links.insert(0, url2)

for url in links:
    rep = requests.get(url)
    # content = rep.text.encode(rep.encoding).decode('utf-8')
    # # 直接用requests时，中文内容需要转码

    soup = BeautifulSoup(rep.content, 'html.parser')

    #table = soup.table[1]
    table = soup.find_all('table')[1]  # 两种方式都可以

    trs = table.find_all('tr')
    trs2 = trs[1:len(trs)]
    list1 = []
    for tr in trs2:
        td = tr.find_all('td')
        row = [i.text for i in td]
        list1.append(row)

    with open('Aggregate_External_Billing4.csv', 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(list1)