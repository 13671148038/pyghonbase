i = [3, 4, 34, 45, 23, 45, 2, 5, 76, 45, 8, 56, 3, 2]
# 选择排序
bs = len(i) - 1
for a in range(len(i) - 1):
    item = i[0]
    index = 0
    for b in range(bs):
        if i[b + 1] > item:
            item = i[b + 1]
            index = b + 1
    if index != bs:
        temp = i[index]
        i[index] = i[bs]
        i[bs] = temp
    bs = bs - 1
print(i)
# 冒泡排序
length = len(i)
for a in range(length - 1):
    for b in range(length - 1 - a):
        temp = i[b]
        temp2 = i[b + 1]
        if temp > temp2:
            i[b + 1] = temp
            i[b] = temp2
print(i)
