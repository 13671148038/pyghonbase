from urllib import request
from http.client import HTTPResponse as result
import time

url = "https://www.baidu.com/s?wd=http%3A%2F%2Fwww.2ge.cn%2Fhome%2Fwdr%2FEF0AAB841ABCD83673FBE58F6E7BCA26"
headers = {'User-Agent',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers=headers)
result2 = request.urlopen(url)
print(result2.read())
