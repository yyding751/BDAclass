#tuple(數組)
#####不可變更
tup = tuple()
print(tup)
tup2 = ()
print(tup2)
tup3 = tuple([1,2,3])
print(tup3)
tup4 = (2,4,6)
print(tup4)

a = (2,[4,6],(1,2,3))
b = a[1:3]
c = a[2][1]

#拆解(unpack)串列或數組中的元素
tup = (3, False, 'ABC')
##變數個數對應數組內元素個數
a,b,c = tup
print(a)
print(b)
print(c)
##變數個數&數組內元素個數不相同，*為剩餘全部
a, *b = (1,3,5,7,9)
print(a)
print(b)
x, *y, z = (2,4,6,8,10)
print(x)
print(y)
print(z)



#set
###唯一性
##集合用{}表示
##想見利空集合要用set()函式，{}被視為空字典dict
##可改變內容
A = set()
A.add(3)
A.add('ABC')
A.add(False)
print(A)
print(3 in A)
##沒有順序
X = {'a','b',1,2}
Y = {1,2,'a','b'}
print(X==Y)
print(X)
print(Y)
##不可重複
S1 = {1,1,2,2,2,3,3,5,6,6,6}
S2 = {6,3,1,5,2,2,5,1}
print(S1==S2)
print(S1)
print(S2)
##set沒排序所以不支援順序相關運算，但可以用差集(-)!!!
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7}
print(S1-S2)


#%%
#dict(字典)
##{"key":value}(鍵：值)
#屬於mapping type(對映型態)

#元素沒有順序
X = {'A':567, 'B':789}
Y = {'B':789, 'A':567}
print(X==Y)

A = {'one':1, 'two':2, 'three':3}
B = dict({'three':3,'one':1,'two':2})
C = dict(one=1, two=2, three=3)
D = dict([('two',2),('one',1),('three',3)])
print(A==B==C==D)

#新增dict[key]=value、刪除del dict[key]
A = {}
A['1'] = 10
A['2'] = 20
del A['1']
print(A)
X = A['2']
print(X)
A['2'] = 200
print(A['2'])

#支援==、!=，支援in以檢查是否指定的鍵是否存在於字典
A = {'a':1,'b':2,'c':3}
B = {'a':7,'b':2,'c':9}
print(A['a']==B['a'])
print(A['b']==B['b'])

print(1 in A)
print('a' in A)

##相關函式keys() values() items()
dicc = {'X':12, 'Y':34, 'Z':56}
print(dicc)
print(dicc.keys())
print(dicc.values())
print(dicc.items())

#%%

lista = [1,5,3]
tupleb = (2,6,4)
setc = {7,9,8}
dictd = {'a':123,'b':456,'c':789}

#迴圈與容器形態處理
for i in lista:
    print(i)

for j in tupleb:
    print(j)

for k in setc:
    print(k)

for z in dictd:
    print(z)

for x,y in dictd.items():
    print(x,y)

#enumerate()函式與容器型態
for i in enumerate(lista):
    print(type(i))
    print(i)
    
for i,j in enumerate(lista):
    print(type(i),type(j))
    print(i,j)



