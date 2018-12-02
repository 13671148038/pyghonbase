squares = [1, 2, 3, 4, 5, 6]
print(squares[1],type(squares))
del squares[1]
print(squares)
squares.remove(1)
print(squares)
squares2 = [90, 98]
print(squares + squares2)
# 数组是可变的
squares = [12, 34, 64, 66, 565]
squares[2] = 4444
print(squares)
# 添加元素
squares.append(33)
print(squares)
# 指定索引出添加元素
squares.insert(0, 5454)
print(squares)
# 排序  只支持int类型的集合
squares.sort()
print(squares)
# 获取几个长度
print(len(squares))
# 二维数组
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1)
print(list1[3][1])

# 开始变成  便利打印1都10

names = ["name", ["saving0", 2000]]
p1 = names.copy()
p2 = names.copy()
p1[1][1] = 200
print(p1)
print(p2)

rr = (1, 2, 3, 4, 5)