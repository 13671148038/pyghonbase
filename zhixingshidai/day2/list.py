list_1 = [1, 2, 3, 4, 5, 5, 4, 2, 6, 7]

list_2 = [5, 6, 7, 8]

print(type(list_1))

set_1 = set(list_1)

print(set_1, list_1)

print(list_1.extend(list_2))
name = "sdcsdcsdcsd"

from collections import deque

list_3 = deque(list_2)
print(type(list_3))
list_3.append(56)
list_3.popleft()

squares = []

for x in range(2, 10):
    squares.append(x ** 2)
print(squares)

squares = list(x ** 2 for x in range(10))

print(squares)

squares = list((x, y) for x in [1, 2, 3] for y in [4, 5, 6])

n = ['hhcsd', "csdcsdc", "dcsdcdsc"], [1, 2, 5]
print(n)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for x in range(2, 52, 5):
    print(x)


a = list(range(10))

print(a)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)



