import urllib.request  as  url2
import urllib
#

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
values = {"username":"626014896@qq.com","password":"kenxzlllxx"}
url="https://www.zhihu.com/"
data=urllib.parse.urlencode(values).encode(encoding='UTF8')
headers = { 'User-Agent' : user_agent }

request=url2.Request(url,data,headers)
response=url2 .urlopen(request)

print(response.read())
print(data)
