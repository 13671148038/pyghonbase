# r 代表防止一切的转义
name = r'C:\file\name'
print(name)

# 字符串截取
stri = "zuguowoaini"
# 获取索引是1的字符
var = stri[1]
print(var)

# 获取指定范围的字符串
var = stri[0:4]
print(var)
# str[3:] 代表是从索引是3到最后  str[:5] 代表从开头到索引是5

# 获取字符串的长度
length = len(stri)
print(length)

# 打印出来是换行的
text = '''
        你好啊!
        我是朱少鹏,
        请多指教
'''
print(text)

# 打印出来是不换行的
text2 = ('你好啊!'
         '我是朱少鹏'
         '请多指教'
         )
print(text2)

# 格式化1
string1 = 'name:{0},age{1},sex;{2}'
print(string1.format("李四", 32, '男'))
string1 = 'name:{name},age{age},sex;{sex}'
print(string1.format(name="王五", age=32, sex='男'))

# 格式化2 一个%s 代表后面一个参数
string1 = 'name: %s,age;%s,sex: %s' % ("娃哈哈", 55, '白')
print(string1)
name = 'lisi'
age = 43
print(f'my name id {name}, nianling  id {age}')

# ================================================================================================================================
# string的 method
string2 = 'I like python DAXIE'
# 返回的字符串第一个字大写  其他的小写
a = string2.capitalize()
print(a)

# 返回字符串小写
string2 = 'I like python DAXIE'
a = string2.casefold()
print(a)

# 参数是一个参数是长度 如果长度大于字符串就在字符换两端添加后面制定的字符
string2 = 'I like python DAXIE'
print(string2.center(25, "o"))

# 获取制定的字符串在后面给你范围内出现的次数
string2 = 'I like python DAXIE'
print(string2.count("o", 5, len(string2)))

# 判断是不是以指定的字符串结尾
string2 = "adcsadcasdf"
print(string2.endswith("df"))

# 判断是不是以指定的字符串结尾
string2 = "adcsadcasdf"
print(string2.startswith("ad"))

# 查找字符串返回索引 没有返回-1
string2 = 'helloworld'
print(string2.find('wo'))
# 返回指定字符串的索引如果没有报错
print(string2.index("w"))

# 判断字符串是否只包含字母和数字 是的话返回true  否则返回false
string2 = "kjk43j"
print(string2.isalnum())




