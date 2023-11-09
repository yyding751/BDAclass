'''
請使用迴圈敘述撰寫一程式，
讓使用者輸入一個正整數a,
利用迴圈計算從1到a之間(包含a)，
所有7的倍數數字總和
'''

#使用者輸入一個正整數
integer = eval(input('Enter an positive integer:'))
#總和初始值為0
total_sum = 0
#計算7的倍數數字總和
for num in range(0,integer + 1,7):
    total_sum += num
print('從1到', integer, '的總和是：', total_sum, sep="")