def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = str(input(prompt))
        if ok in ['y', 'yes', 'ye']:
            return True
        if ok in ['n', 'no', 'nop', 'nope']:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        else:
            print(reminder)


# res = ask_ok('Do you really want to quit?')

i = 5


def f(arg=i):
    print(arg)


# 打印的5
f()


#
def f(a, l=[]):
    l.append(a)
    return l


print(f(2))
print(f(3))
print(f(4))


def f(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l


print(f(2))
print(f(3))
print(f(4))

r = [2, 4]
l = list(range(*r))
print(l)


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


p = {'voltage': '45v', 'state': 'sds', 'action': 'asdcsdc删除'}
parrot(**p)


# 返回一个函数
def f(n):
    return lambda x: x + n


a = f(3)
print(a(5))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
key = lambda pairs: pairs[1]
pairs.sort(key=lambda pair: pair[0], reverse=True)
print(pairs)


def d():
    """
    scsdc
    sdc
    :return:
    """
    pass


# 打印方法注释
print(d.__doc__)


def f(ham: str, eggs: str = 'eggs') -> str:
    return 'scsdc'


# 打印方法参数个返回值类型
print(f.__annotations__)
