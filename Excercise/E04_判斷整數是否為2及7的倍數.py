#Excercise_4
'''
請使用選擇敘述撰寫一程式，
讓使用者輸入一個整數，
然後判斷他是否為2或7的倍數。
'''

int = eval(input('Please enter an integer:'))
if int % 2 != 0 and int % 7 != 0:
    print(int,'不是 2 也不是 7 的倍數')
elif int % 2 == 0 and int % 7 == 0:
    print(int,'是 2 及 7 的倍數')
elif int % 2 == 0:
    print(int,'是 2 的倍數')
else:
    print(int,'是 7 的倍數')
    
    
    
#Update
num = eval(input('Please enter an integer:'))
if num % 2 == 0 and num % 7 == 0:
    print(num,'是2及7的倍數', sep='')
elif num % 2 == 0:
    print(num,'是2的倍數', sep='')
elif num % 7 == 0:
    print(num,'是7的倍數', sep='')
else:
    print(num,'不是2也不是7的倍數', sep='')