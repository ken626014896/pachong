import urllib.request  as  url2

import http.cookiejar as  Cookielib

#1）获取Cookie保存到变量
#声明一个CookieJar对象实例来保存cookie
cookie=Cookielib.CookieJar()
#利用url2库的HTTPCookieProcessor对象来创建cookie处理器
handler=url2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener=url2.build_opener(handler)

response=opener.open("http://www.baidu.com")

for item  in cookie:
    print  ("Name = "+item.name)
    print("Value ="+item.value)

#2）保存Cookie到文件
filename="cookie.txt"
cookie2=Cookielib.MozillaCookieJar(filename)

handler2=url2.HTTPCookieProcessor(cookie2)

opener2=url2.build_opener(handler2)

response2=opener2.open("http://www.baidu.com")

cookie2.save(ignore_discard=True,ignore_expires=True)

#3）从文件中获取Cookie并访问
cookie3=Cookielib.MozillaCookieJar()

cookie3.load('cookie.txt', ignore_discard=True, ignore_expires=True)

req=url2.Request("http://www.baidu.com")

opener3=url2.build_opener(url2.HTTPCookieProcessor(cookie3))
response3=opener3.open(req)

print(response3.read())
