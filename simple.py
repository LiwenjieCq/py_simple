#!/usr/bin/env python3
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-

print("hello","world")
print("100 + 200=" , 100 + 200)
# name = input("Please input your name:")
# print(name)
print('I\'m learning \npython')
# \\表示的字符就是\
print('\\\n\\')

print(r"\\\n\\")

print(not True)

print(None)

# 不用定义属性类型
t_01  = True
print(t_01)


# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

# 对bytes类型的数据用带b前缀的单引号或双引号表示
print("ABC".encode('ascii'))
print("中文".encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode("utf-8", errors='ignore'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8")))
print(len("中文"))


# 格式化
print("My name is %s, I'm %d years old." % ("Vinge",20))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print( 'Age: %s. Gender: %s' % (25, True))

classmates = ['Michael', 'Bob', 'Tracy']
# 取最后一个元素
print(classmates[-1])