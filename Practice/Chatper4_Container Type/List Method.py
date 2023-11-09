#list串列，串列內為元素，元素有順序
lis = []
print(lis)
lis = list()
print(lis)

lis = ['ABC',False,2,1.5]
print(lis)
##set有格式上的排序，用大括弧順序會跑掉
lis = list({'21',True,5})
print(lis)

L = [2,4,6,8,10,12,14,16,18]
del L[2]
print(L)

del L[2]
print(L)


#a整數串列、b混合資料型態的串列、c空串列
#d多為串列、e串列結合
a = [1,5,9]
b = [2,3.5,6.5,'Hi']
c = []
d = [18,[a,b]]
e = a + b

b[0]=9
print(b)
u = a[1:3]
x = d[1]
y = d[1][1]
z = d[1][1][1]
print(y)

print([123]+[456])
print([123]+[True,'abc'])
print([123]*2)
print([123]*0)
print([123]*-1)
print([123]*2.5)
print([123]*-2.5)

print([1,3]==[3,1])
print(['A']>=['a'])
print(['b']!=['B'])

print(2 in [1,2,3])
print('A' in ['AB','BC'])
print('AB' in ['AB','BC'])


#串列建構list conprehension
##利用迴圈產生大量有規律性的元素
listc = [i for i in range(5)]
print(listc)

listc1 = [j+3 for j in range(5)]
print(listc1)
listc2 = [k for k in range(3,8)]
print(listc2)


print(len([1,2,3,4]))
print(min([1,2,3,4]))
print(sum([1,2,3,4]))

#list相關函式
num1 = [1,3,5,7,9]
num2 = [2,4,6,8,10]
##list.append()附加到最後
num1.append(11)
print(num1)
##list.extend(x)將x中元素附加到list最後
num1.extend(num2)
print(num1)
##
print(num1.count(11))
##
print(num1.index(9))
##
num1.insert(2,100)
print(num1)
########list.pop([])取出list中"索引值"為i的元素，預設為最後一個
num1.pop()
print(num1)

num1.pop(5)
print(num1)
#list.remove()
num1.remove(5)
print(num1)
#list.reverse()
num1.reverse()
print(num1)


#串列排序
##sort直接修改原list並排序
##sorted回傳排序好的新串列
X = [1,3,2,4,5]
print(sorted(X))
print(X)

X.sort()
print(X)
