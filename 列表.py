a = ['hello','python',4523,"淦"]#列表
print(a)
print(a[0:3]) #访问第一到三个元素
print(a[-1]) #访问最后一个元素
print(a[0].title(),"world !")



######### 修改列表中的元素
print(a)

a[0] = "Hello python's world"
print(a)


######### 添加列表元素

print(a)
a.append('林') #末尾添加元素
print(a)
a.insert(1,'py')#列表中插入元素


######### 删除列表元素

print(a)
del a[1] #删除列表第二个元素
print(a)
del a #删除列表元素
a = ['hello','python',4523,"淦"]
print(a)

b = a.pop() #删除列表最后一个元素，并保存在变量b中
print(b)
print(a)
b = a.pop(0) #删除列表中指定元素，并保存在变量b中
print(b)
print(a)

a = ['hello','python',4523,"淦"]
a.remove('python') #根据值来删除列表中元素（只删除第一次出现的元素）
print(a)


######## 改变列表顺序

cars = ['bmw','audi','toyota','subaru']
cars.sort() # 永久 按字母顺序排列元素
print(cars)
cars.sort(reverse = True)# 永久 按字母 逆序 排列元素
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(sorted(cars)) # 对列表暂时进行排序
print(cars)
print(sorted(cars,reverse = True))

cars = ['bmw','audi','toyota','subaru']
cars.reverse() # 反转列表中的元素
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(len(cars)) # 确定列表长度


########  操作列表

cars = ['toyota', 'subaru', 'bmw', 'audi']

for i in cars:
    print(i)


#######  创建数值列表


for value in range(1,5):
    print(value)
print('\n')

number_1 = range(1,6)
for value in number_1:
    print(value)
print('\n')

number_2 = range(1,11,2) # range（从1开始，到11结束（不包括11），步长为2）
for value in number_2:
    print(value)
print('\n')

number_3 = list(range(1,11))
squares = []
for value in number_3:
    square = value ** 2  # ** 表示乘方 
    squares.append(square)
for value in squares:
    print(value)

print(type(number_1))  # <class 'range'>
print(type(number_3))  # <class 'list'>
print("\n")


#######  对数字列表进行简单的统计计算

digits = [12,34,654,2,54,63,213]
print(max(digits))
print(min(digits))
print(sum(digits),'\n')


#######  列表解析

Squares = [value ** 2 for value in range(1,20,2)]
    #首先指定一个描述性的列表名，如squares;然后，指定一个左方括号，
    #并定义一个表达式，用于生成你要存储到列表中的值。
print(Squares,'\n')


#######  使用列表的一部分（切片）

rooms = ['a','b','c','d','e','f']
print(rooms[0:4:1]) # 从第一个元素到第四个元素（包含第四个），步长为1
print(rooms[:4]) # 不指定第一个元素，默认从列表首元素开始
print(rooms[0:]) # 不指定最后一个元素，默认提取到列表末尾元素
print(rooms[-4:])
print(rooms[5]) # 指定某一元素
print('\n')

for room in rooms[1:5:2]: #切片遍历
    print(room)
print('\n')

my_rooms = rooms[1:4:2]
print(my_rooms)

ff = [1,2,3,4,5]
kk = [ff]
for i in range(1,11):
    kk.append(i)
for i in range(0,len(kk)):
    if i == 0:
        for j in range(0,len(ff)):
            print(ff[j])

    else:
        print(kk[i])
print(kk)

Q = []
for i in range(0,10):
    Q.append([])
for i in range(0,10):
    for j in range(1,11):
        Q[i].append(j)
print(Q)
for i in range(0,len(Q)):
    print(Q[i])