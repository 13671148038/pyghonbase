# 定义字典就是java中的map集合

info = {
    'name': '李四',
    "age": '32',
    "sex": '男',
    "pho": '13671142368'
}

for k in info:
    print(k, info.get(k))

info2 = {
    3: 3,
    4: 4,
    "cds": "3434",
    "dd": {
        "sdc": 555,
        "fgr": 677
    }
}
print(info)

# 存在就替换之前的值,不存在就添加
info['name'] = '王五'

# 删除
del info["name"]
print(info.get("age3"))
print('age' in info)
# 将两个字典合并一个
info.update(info2)
print(info.items())
print(repr(info))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(name, phone)

for x in range(1, 11):
    print('{0:2d} {1:2d} {2:3d}'.format(x, x * x, x * x * x))
name = 'sdsd'
print(name.rjust(50), name)
print(name.zfill(5))
