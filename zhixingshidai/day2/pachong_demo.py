from urllib import request
from http.client import HTTPResponse as result
import time

url = "https://search.jd.com/Search?keyword=%E6%B5%B7%E5%B0%94%E7%A9%BA%E8%B0%83&enc=utf-8&spm=a.0.0&pvid=ba4b67658ef34daab5d36af05e4f9583"
headers = {'User-Agent',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers=headers)
result2 = request.urlopen(url)
b = bytearray(500)
print(b)
print(result2.readinto(b))
print(b.decode())
