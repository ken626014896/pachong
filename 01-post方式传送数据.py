import urllib.request  as  url2
import urllib


#
values = {"username":"1016903103@qq.com","password":"XXXX"}
url="http://www.taobao.com"
data=urllib.parse.urlencode(values).encode(encoding='UTF8')
request=url2.Request(url,data)
response=url2 .urlopen(request)

print(response.read())
print(data)
