# if 语句
a = 5
if a < 5:
    print('我是小于五的')
elif a != 5:
    print('我等于五')
else:
    print("我是大于无的")

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

#     for
for i in range(7, 9):
    print(i)
squraes = [12, 324, 4, 57, 99, "sdsd"]
for item in squraes:
    print(item)


def fib(n):
    a = 0
    b = 1
    result = []
    while a < n:
        print(a)
        result.append(a)
        a, b = b, a + b


fib(1000)


def fffff(name, age=52, sex="nan"):
    print(name)
    print(age)
    print(sex)


fffff(888, 5555)

import getpass

# ussername = input("name:")
# password = getpass.getpass("password")
#
# print(ussername, password)

if not None:
    print(343333333333)

