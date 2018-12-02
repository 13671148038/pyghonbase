# if 语句
a = 6
if a < 5:
    print('我是小于五的')
elif a != 5:
    print('我等于五')
else:
    print("我是大于无的")

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

for x in raw_data:
    if math.isnan(x):
        print(x)

a = 9
b = 0
while b < a:
    print(b)
    b = b + 1
