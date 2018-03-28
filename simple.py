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

# list 可存放不同类型的数据
classmates = ['Michael', 'Bob', 'Tracy']
# 增加元素
classmates.append("Vinge")
# 插入到指定位置
classmates.insert(1,"Insert")

# 删除最后一个元素
classmates.pop()

# 删除指定一个元素
classmates.pop(1)

# 取最后一个元素
print(classmates[-1])
print(classmates)

# tuple 元组 定长，不可变相对list更安全 注意括号
t = ("Tom", "Coco", "Lili")
# 消除歧义
a = (1, )

# 这种情况的list属于可变元素
b = ('a', 'b', ['A', 'B'])

# for
for name in b:
    if len(name) > 1:
        for list_name in name:
            print(list_name)

# range()函数生成一个整数序列
sum = 0
for i in range(0, 101):
    sum += i
print(sum)

# while True : {print(1)}

# dict 空间换时间 java中的map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 通过in判断key是否存在
print("Michael" in d)

# 返回的None自己指定value
print(d.get("test",-1))
d.pop('Michael')
print(d)

# set 自动去重
s = set([1, 2, 3])
print(s)
s1 = set([1, 2, 3])
s2 = set([4, 2, 3])
print(s1 & s2) #交集
print(s1 | s2) #并集

# 删除key 添加key
s.remove(1)
s.add("123")
print(s)

#函数
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))


def my_fun(x):
    if x == 0:
        return 0
    else:
        return 1
print(my_fun(0))

# pass占位符
def nop():
    pass
print(nop())

# 数据类型检查函数isinstance()

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(0))

# 定义可变参数,在参数前面加了一个*号

# 切片 java中的substring
L = list(range(100))
print(L[0:10])

# 迭代
e = {'a': 1, 'b': 2, 'c': 3}
for key in e:
    print(key)

# 判断一个对象是否可以迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# 获取索引
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
# 双层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

# 获取指定目录所有文件
# listdir()
import os
print([d for d in os.listdir("../../")])

# items()
# dict的items()可以同时迭代key和value 列表生成式也可以使用两个变量来生成list
f = {'x': 'A', 'y': 'B', 'z': 'C' }
print([x + "=" + y for x, y in f.items()])

# 生成器
g = (x * x for x in range(10))
print(next(g))
for h in g:
    print(h)

def fbl(m):
    n,a,b = 0,0,1
    while n <= m:
        # 包含yield关键字即为一个generator
        yield b
        a, b = b, a + b
        n = n + 1
        if n == m:
            print(a)

    return "done"

print(fbl(10))

fi = fbl(10)
for fi in fi:
    print(f)
print(abs)