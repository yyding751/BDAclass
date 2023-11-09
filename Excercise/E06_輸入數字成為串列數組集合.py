'''
請撰寫程式，輸入欲產生的個數，
之後依序輸入其個數存於串列，再將此串列排序後，
轉為數組與集合，分別印出。
'''
i=1
lista = []
rand = eval(input('請輸入欲產生的個數：'))
num = eval(input('請輸入第%d個數字：'%(i)))
lista.append(num)
while i < rand:
    i=i+1
    num = eval(input('請輸入第%d個數字：'%(i)))
    lista.append(num) 
lista.sort()
print(lista)
print(tuple(lista))
print(set(lista))
