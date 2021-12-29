# coding=utf-8
a = "hello " + "world" + "!"

print(a.title())#每个单词首字母大写（不改变变量值）
print(a)
print(a.upper())#每个字符变为大写（不改变变量值）
print(a)
print(a.lower())#每个字符变为小写（不改变变量值）


###############
b = "   abc    abc    "
print(b)
print(b.rstrip())#删除右边末尾的空格（不改变变量值）
print(b)
print(b.lstrip())#删除左边开头的空格（不改变变量值）
print(b)
print(b.strip())#删除开头和末尾的空格（不改变变量值）
print(b)

###############
c = input("请输入一个整数：")
print(c)
