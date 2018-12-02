# 定义函数

def add(x):
    "参数加一"
    return x + 1


print(add(5))


def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid value response")
        print(reminder)


# ask_ok("opreate:")

i = 5


def f(arg=i):
    print(arg)


i = 6
# 打印的是5
f(666)
f()


def app(a, L=[]):
    L.append(a)
    return L


print(app(4))
print(app(4))
print(app(4))


def app(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(app(4))
print(app(5))
print(app(6))
print(app(7))


def f2(a, b='lisi', c='43'):
    print(a, b, c)


f2(58, b="sdcsdc")


def f3(a, *b, **c):
    print(a)
    for v in b:
        print(v)
    for kw in c:
        print(kw, ':', c.get(kw))


f3(44, '你好', 343, n=4, t=6, lll=66)


# 返回lambda表达式
def f4(n):
    """啊上档次三大城市的"
    "啊上档次三大城地方的的v市的"
    "啊上档次三大城市的"""
    return lambda x: x + n


f = f4(50)
print(f(52))
print(f(5))

squares = [4, 5, 3, 3, 2, 5, 6]
squares.sort(key=lambda pair: pair)

print(squares)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
print(f4.__doc__)
