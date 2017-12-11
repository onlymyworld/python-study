import urllib
from bs4 import BeautifulSoup
import requests
import csv
import os,sys



url2 = 'Asset_Value_by_period.htm'
# address =['Asset_Value_by_period.htm','Billing_data_(universal).htm']

#fold = ['CRM','service','GSC','finance']
fold = ['GSC']
#address =['Asset_Value_by_period.htm','Billing_data_(universal).htm']
links = []
for n in range(2, 40):
    # 页面总数为39页，需要自己先从网页判断，也可以从页面抓取，后续可以完善
    link = url2 + str(n)
    links.append(link)
links.insert(0, url2)
for item in fold:
    address = os.listdir('F:/DDIC/DDIC/scr/'+item+"/")
    for url in address:
        #rep = requests.get(url)
        rep = open("F:/DDIC/DDIC/scr/"+item+"/"+url, 'r',encoding='UTF-8')
        htmlpage = rep.read()

        # content = rep.text.encode(rep.encoding).decode('utf-8')
        # # 直接用requests时，中文内容需要转码

        soup = BeautifulSoup(htmlpage, 'html.parser')

        #table = soup.table[1]
        tables = soup.find_all('table')  # 两种方式都可以
        table = soup.find_all('table')[0] 
        #if(len(tables) >1):
        # table = soup.find_all('table')[1] 
        
        
        aaa = url.split('.')
        bbb = url.split('.')
        if(len(aaa) > 1):
            bbb = url.split('.')[0]
        trs = table.find_all('tr')
        trs2 = trs[0:len(trs)]
        list1 = []
        for tr in trs2:
            td = tr.find_all('td') 
            row = [i.text for i in td]
            list1.append(row)

        with open("F:/python/"+item+"/"+bbb+'.csv', 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(list1)