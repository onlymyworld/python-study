#coding=utf-8
import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	return imglist

	

html = getHtml("http://www.baidu.com")

print getImg(html)