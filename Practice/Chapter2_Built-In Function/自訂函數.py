#自訂函數_參數與引數的數目要相符
def sayhello(x):
    print("hello!111")
    print("hello!")
    print("hello!")

sayhello(1)
sayhello("1")
sayhello(3.1415926)
sayhello(3.14>1)

#函數的參數(制定)與引數(呼叫)不同
def ctof(degreeC):
    degreeF = degreeC *1.8 + 32
    print("攝氏",degreeC,"度可以轉換成華式",degreeF,"度")

temperatureC = eval(input('輸入攝氏溫度可轉換成華氏溫度：'))
ctof(temperatureC)
print('轉換結束')

#關鍵字引數_計算體積
def Volume(lenth, width, height):
    print("體積積為",lenth*width*height)

Volume(10,20,5)
Volume(10,height=5,width=20)

#預設引數值
def teatime(meal,drink='紅茶'):
    print('餐點為',meal,',飲料為',drink, sep='')
    
teatime('牛排')
teatime(drink='鮮奶茶',meal='鮪魚蛋餅')


#變數的有效範圍
##全域變數：定義在函式外面，範圍是一整個模組
##區域變數：定義在函式裡面，範圍是一整個函式
X=100
def test():
    X=200
    print(X)
test()

X=100
def test():
    print(X)
test()

X=100
def test():
    X=200
    print(X)
test()
print(X)

#函式的回傳_return:將區域變數變成全域變數
def cal(x,y):
    div = x//y
    mod = x%y
    return div, mod
a, b = cal(120,7)
print('120除以7的商數是',a,'而餘數是',b)
c, d = cal(250,15)
print('250除以15的商數是',c,'而餘數是',d) 
