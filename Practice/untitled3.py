#測試 eval input 100, 為tuple
print(type(100,))
context = eval(input('enter a positive number:'))
print(type(context))


#%%
#try...except處理例外
try:
    X = eval(input('請輸入被除數X:'))
    Y = eval(input('請輸入除數Y:'))
    Z = X / Y
    print('X除以Y的結果等於',Z)
except:
    print('無法計算請重新輸入')


#%%
#try...except...else...finally
try:
    X = eval(input('請輸入被除數X:'))
    Y = eval(input('請輸入除數Y:'))
    Z = X / Y
    print('X除以Y的結果等於',Z)
except:
    print('無法計算請重新輸入')
