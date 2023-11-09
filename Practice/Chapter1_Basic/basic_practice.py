print('1+5')
print('''0
.2-0.
3''')
print(3*3)

print(6/3)
print(6/4)
print(6//4)

print(5<3)
print(9>7)

#布林值
print(bool())
print(bool(0))
print(bool(5.9))

print('bool(False)')
print('''bool(None))
print(bool(True)''')

print(bool(()))
print(bool([]))
print(bool({}))

#跳脫字元
print('it is')
print('It\'s wonderful.')
print('a\\b test')
print('\"They\" are over there.')
print('It is a \tcat.')
print('This is an \nadorable kitten.') 
print('How\'s the weather?')

#=賦值
todayWeather='Windy'
print(todayWeather)
#指派變數練習
num1=521
num2=37
num3=num1+num2
print(num3)
num2=True
num3=num1+num2
print(num3)

#算術運算子練習
'''%取餘數、//取商數、**為指數運算'''
print('157'*5)
print('157'+'324')
print(5%2)
print(5/2)
print(5//2)
print(2**5)

#比較運算子練習
'''
==為若a等於b則回傳True
!=若a不等於b則回傳True
'''
print(35==(30+5))
print(35!=(30+5))

#邏輯運算子練習(真值表)
'''
邏輯合取(AND):若兩值皆為True則回傳True
邏輯或(OR):若兩值有一為True則回傳True
'''
print((3>2)and(1>2))
print((3>2)or(1>2))
print(not(3>2))

#指派運算子練習
x,y,z=3,2,1
print(x=x+y)

x,y,z=3,2,1
x*=y
print(x)

#函數內的參數value(s),sep,end
'''
選擇性參數sep預設值為空一格
選擇性參數end預設值為\n(換行)
'''
x,y,z=3,2,1
print(x)
print(y)
print(z)
print(x,y,sep=':::')
print(z)
print(x,y,sep=':::',end='$$$')
print(z)

#輸入函數input
'''
輸入函數內的提示句為選擇性參數,且default type
eval函數會將input函數取得的string轉換為數值type like int, float, bool，或變數(需先設定)
eval函數可直接進行運算
'''
weather=input('How\'s the weather?')
num=input('what time is it?')
num=eval(input('what time is it?'))

abcde=999
times=input('how many times?')
    ##練習計算圓面積
PI=3.14159
radius=eval(input('What\' the radius of this circle?'))
print('The square of this circle is', PI*radius*radius)

#通用格式化 %(pronounce:par) (十進位整數d,十進位浮點數f,字串s)
print('It\'s %s today.'% 'windy')
print('%4d除%4d是%4.3f' % (35,2,35/2))
    ##整數全部都會print
print('%2.3f'%12345.12345)

#Python專用格式化
'''{:格式化方式}.format(數字/字串)'''
    ##小數&顯示正負號
print('{:5.7f}'.format(3.14159))
print('{:+5.7f}'.format(3.14159))
print('{:5.0f}'.format(3.14159))
    ##左/右邊補0
print('{:0>5d}'.format(3))
print('{:0<5d}'.format(3))
    ##左右中間對齊&百分比格式
print('{:10d}'.format(3))
print('{:<10d}'.format(3))
print('{:^10d}'.format(3))
print('{:.2%}'.format(3))
    ##千元表示&科學符號
print('{:,}'.format(3000000000))
print('{:.2e}'.format(3000000000))
    ##十進位轉換為二&八&十六進位
print('{0:d},{1:b},{2:o},{1:x}'.format(83,83,83))
    ##除式練習
print('{0:d}除以{1:d}等於{2:.4f}'.format(10,3,10/3))
print('{0:5d}除以{1:5d}等於{2:5.4f}'.format(10,3,10/3))
    ##除式練習(指派變數)
print('{n1:d}除以{n2:d}等於{r:.4f}'.format(n1=10, n2=3, r=10/3))
print('{n1:<5d}除以{n2:<5d}等於{r:.4f}'.format(n1=10, n2=3, r=10/3))
print('{n1:5d}除以{n2:5d}等於{r:.4f}'.format(n1=10, n2=3, r=10/3))
print('{n1:!^5d}除以{n2:?^5d}等於{r:.4f}'.format(n1=10, n2=3, r=10/3))
