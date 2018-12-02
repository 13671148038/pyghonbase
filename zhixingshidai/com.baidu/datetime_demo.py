# date 只有年月日
from datetime import date

# 获取当前时间
now = date.today()
# 年
print(now.year)
# yue
print(now.month)
# 日
print(now.day)
# 时间格式化
strdate = now.strftime('%Y-%m-%d')
print(strdate)
# 自定义时间
br = date(2003, 5, 6)
print(br)
# 比较时间是否相等
print(now == br)

from datetime import datetime

dt = datetime.today()
print(dt.isoformat())
print(dt.strftime("%Y-%m-%d %H:%M:%S"))