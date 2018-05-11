# -*- coding: UTF-8 -*-
import urllib.request  as  url2

import http.cookiejar as  Cookielib


import  urllib

filename="zhihucookie.txt"
cookie=Cookielib.MozillaCookieJar(filename)

opener=url2.build_opener(url2.HTTPCookieProcessor(cookie))

values={"username":"626014896@qq.com","password":"kenxzlllxx"}
postdata=urllib.parse.urlencode(values).encode(encoding='UTF-8')

loginurl="https://www.zhihu.com/"
#模拟登录，并把cookie保存到变量
result=opener.open(loginurl,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址

gradeurl="https://www.zhihu.com/explore"

result=opener.open(gradeurl)

print(result.read())
