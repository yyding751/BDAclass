#Exercise_3
'''
請撰寫程式，
將使用者輸入的兩個整數作為參數傳遞給一個名為 compute(x, y) 的函式，
此函式將回傳 x 和 y 的乘積。
'''

def compute(X, Y):
    product = X*Y
    print(product)
a = eval(input('請輸入一個整數:'))
b = eval(input('請再輸入一個整數:'))
compute(a,b)



def compute(x, y):
    product = x*y
    return product
a = eval(input('請輸入一個整數:'))
b = eval(input('請再輸入一個整數:'))
print(compute(a,b))
