#de func_name(p1,p2,p3,...):

def acc_sum(n): #可以不返回值 编译器不关心是否有返回值
    _sum = 0

    for i in range(n):
        _sum += i
    return _sum


a = acc_sum(2020) #0加到2019
print(a)
print(acc_sum(2020))
print()
