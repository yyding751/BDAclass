#iterator：迭代，有順序、可反覆運算的物件 e.g.range()

#While迴圈
##當重複次數難以計算
word = input('請輸入「快樂」的英文：')
while word.upper() != 'HAPPY':
    word = input('答錯了，請重新輸入「快樂」的英文：')    
else:
    print('答對了!')

#range() 數字
##range(start, end, step)
list(range(5))
list(range(2,5))
list(range(5,-17,-3))

#for迴圈(計數迴圈)
##當已知重複次數
##for var in iterator

for i in range(3,13,4):
    print(i)
    
name='Andrew'
for i in range(len(name)):
    print(i,name[i])
    
name='Andrew'
for i in name:
     print(i)   

#break敘述：在迴圈內，強制離開迴圈，經常配合條件判斷使用
word = input('請輸入「天氣」的英文：')
while word.upper() != 'WEATHER':
    if word.upper() =='QUIT':
        print('已結束遊戲')
        break
    word = input('不正確，請重新輸入「天氣」的英文，可輸入QUIT結束遊戲：')
else:
    print('Right!')

#continue敘述：在迴圈內，跳過後面敘述，直接返回迴圈開頭
i=0
while i<50:
    i=i+7
    if i % 3 != 0:
        continue
    print(i,'是30以內的3與7的公倍數',sep="")
