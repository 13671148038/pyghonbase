
# python 中变量定义有三个范围
# 第一个就是直接定义如:spam = "local spam"  这个变量的范围就是只在定义范围内 称为局部作用域
# 第二个定义的关键字:nonlocal spam  外层函数的局部作用域就是在方法do_nonlocal外层可以用
# 第三个定义的关键字:global spam  当前模块的全局作用域
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "do_nonlocal spam"

    def do_global():
        global spam
        spam = "do_global spam"

    spam = '产生的城市'
    do_local()
    print(spam)
    do_nonlocal()
    print(spam)
    do_global()
    print(spam)



scope_test()
print(spam)