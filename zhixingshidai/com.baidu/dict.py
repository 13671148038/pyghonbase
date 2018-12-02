# 定义一个字典
info = {
    'name': '李四',
    "age": '32',
    "sex": '男',
    "pho": '13671142368'
}
# 遍历字典
for key in info:
    print(f"key:{key} value:{info[key]}")

# 存在就替换之前的值,不存在就添加
info['name'] = '王五'
print(info)

# 删除
del info['name']
print(info)

# 判断是否存在
res = 'age' in info
print(res)

info2 = {
    3: 3,
    4: 4,
    "cds": "3434",
    "dd": {
        "sdc": 555,
        "fgr": 677
    }
}
print(info2)
# 将两个字典合并一个
info.update(info2)
print(info.items())
# 转成字符串
print(repr(info))
print(dict(info2.items()).get("sd"))

