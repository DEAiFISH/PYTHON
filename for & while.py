#通过缩进来控制语句块的层次关系
#缩进必须一致

a = [1,2,4,3]
for i in a:
    print(i)
print()

n = 2020
_sum = 0
for i in range(0,20,1): #等价于 range(20)
    _sum += i
print(_sum)
print()

a = [1,4,5,6]
z = 0
for i,x in enumerate(a):
    print(i,x)
    z += a[i]
print(z)
print()

sum1 = 0
i = 1
while sum1 < 5000:
    sum1 += 1
    i += 1
print(sum1)
print()

a = [2,4,5,6]
print(sum(a)) #sum是内置函数 不能定义变量名为sum
print()

a = [1,2,3,4]
b = [5,6,7,8]
c = [0,0,0,0]
for i in range(0,4,1):
    c[i] = a[i] + b[i]
print(c)