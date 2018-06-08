#!/usr/bin/python
# coding=utf-8

import urllib
import urllib2

data = {"lx":'5','bzxr.court_no':'0F1','curPage':'2'}
data = urllib.urlencode(data)

req = urllib2.Request("http://jinanzy.sdcourt.gov.cn/sdfy_search/bzxr/xzbzxList.do",data)
req.add_header('Host','jinanzy.sdcourt.gov.cn')
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0')
req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
req.add_header('Content-Type','application/x-www-form-urlencoded')
req.add_header('Cookie','JSESSIONID=WLcxXhnX29wcGMLDyCWjFykWckjhdpWQKTbhhBdRLpqsylt52HCH!-1496633796; Hm_lvt_27185599d39752a14c512761379da2f1=1470213825; Hm_lpvt_27185599d39752a14c512761379da2f1=1470213865; _gscu_1905082155=702138317nd9sb29; _gscs_1905082155=70213831d7rif229|pv:4; _gscbrs_1905082155=1; ADMINCONSOLESESSION=WwvGXhvNw31QQsZyQl9cdbMjnQQ2J0Y7NCgSX1kBkcmDNT9kGngm!-1496633796')
req.add_header('Referer','http://jinanzy.sdcourt.gov.cn/sdfy_search/bzxr/xzbzxList.do')
req.add_header('Content-Length','32')
resp = urllib2.urlopen(req)
print (resp.read())

# enable cookie
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# response = opener.open(req, data)
# print response.read()
