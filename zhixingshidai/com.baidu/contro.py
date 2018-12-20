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

# break  continue
import operator

arr = list(range(9))
for i in arr:
    if operator.eq(i, 6):
        break
    elif operator.eq(i, 4):
        continue
    else:
        print(i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
        break
    else:
        # loop fell through without finding a factor 如果range(2, n)是是空的就是走else这里
        print(n, 'is a prime number')

for a in []:
    print(a)
else:
    # 会走这里,因为数组为空
    print('sdcs')

