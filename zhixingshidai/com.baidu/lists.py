from collections import deque

# 数组的定义1
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 数组的定义2
squares = []
for x in range(2, 10):
    squares.append(x ** 2)
print(squares)
# 数组的定义3
squares = list(x for x in range(6))
print(squares)

# 数组的定义4
squares = list(map(lambda x: x ** 3, range(10)))
print(squares)

# 根据索引获取数组中的元素
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
item = squares[0]
print(item)

# 删除数组中的元素
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 根据索引删除
del squares[0]
print(squares)
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 删除数组中值是8的元素
squares.remove(8)
print(squares)

# 元素替换
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares[1] = '00099'
print(squares)

# 添加元素
squares = []
# 获取数组的长度
print(len(squares))
# 添加元素
squares.append(4)
squares.append(8)
print(squares)
# 指定索引出添加元素  如果索引指定索引大于数组长度 那么在数组的最后添加
squares.insert(5, 5454)
print(squares)

# 排序
squares = [5, 6, 325, 74, 152]
squares.sort()
print(squares)
# 报错  因为不是阿拉伯数字
# squares = ['rf', 'dfg', 'ki', 'aa']
# squares.sort(squares)
# print(squares)

# 二维数组
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1)
print(list1[3][1])

# 数组的复制
names = ["name", ["saving0", 2000]]
p1 = names.copy()
p2 = names
# 修改p1的值后 p1he p2的值都会改变
p1[1][1] = 200
print(p1)
print(p2)

# 定义集合
list_1 = [1, 1, 1, 2, 5, 6, 36, 5, 4]
# set方法是去除重复
set_1 = set(list_1)
print(type(set_1))
print(set_1)
print(set_1, list_1)
# ======================================================================================================================================================
list_1 = [1, 1, 1, 2, 5, 6, 36, 5, 4]
# 定义一个双向队列  所谓的双向队列就是在左边和右边都可追加和删除元素
list_2 = deque(list_1)
# 获取指定索引处的元素 和list的方法是一样的
print(list_2[1])
# 往后追加
list_2.append(56)
print(list_2)
# 开始处追加
list_2.appendleft(9888)
print(list_2)
# 结尾处删除
list_2.pop()
print(list_2)
# 开始出删除
list_2.popleft()
print(list_2)

squares = list((x, y, z) for x in [1, 2, 3] for y in [4, 5, 6] for z in [4, 5, 6])
squares.sort()
print(squares)

# 这是tuple类型定义以后是不可以改变的
r = (1, 2, 3)
