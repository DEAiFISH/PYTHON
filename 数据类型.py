# coding=utf-8
from sys import getsizeof

a = 1
b = 1234567890123456789
a1 = 2.0

print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(a1))

c = 1
d = 2
print(a / b)
print(a // b)  # 只取整数

e = 'hello'
print(e[0], e[-1], e[2:5], e[2:5:2])  # 从第三个元素（包含）到第五个元素（不包含） 步长为2

f = 'world'
print(e + f)
print(e * 2)

# 列表
g = [1, 2, 4, 3]
print(g[0:4:2], g[-1])  # 【-1】是倒数第一个元素的值
g[0] = 5
print(g[0])
a = [2, 3, 5, 9, 11]
print(a)

a.append(13)
print(a)

a.insert(3, 7)
print(a)

a.remove(11)
print(a)

del a[2]
print(a)

# 元祖 跟列表一样 但不能更改值
h = (1, 2, 3, 4)
print(h)

# 集合 （无序 不能通过下标取值 j[0]）
j = {10, 9, '2', 10}  # 存放了三个值
k = set()  # 空集合
print(j, k)
print(list(j)[0])  # 可以通过强制转换

# 字典
l = {"1": "计算机简史",
     1: "计算机发展简史",
     "5": "程序设计知识",
     "hello": "hello world"}  # 变量l是一个字典，里面存放了两个键值对
print(l['1'], l['5'])  # 键'1'，对应的值是"计算机简史"  键入字符
print(l["hello"])  # 键入字符串
print(l[1])  # 键入整型
print(list(l))  # 用list 获取字典中的键
m = {
    "1": {
        "name": "计算机发展简史",
        "content": {
            "1.1": "hello",
            "1.2": "world"}
    }
}
print(m["1"]["name"])
print(m["1"]["content"]["1.1"], m["1"]["content"]["1.2"])

# if语句 不需要花括号  通过缩进来控制语句块的结构
n = 2
if n < 1:  # 注意 ：
    print(n)
    print("n < 1")
elif n > 1:
    print(n)
    print("n > 1")
else:
    print(n)
    print("n = 1")
