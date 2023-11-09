#Excercise_1
'''
◆請輸入一矩形的長和寬,之後計算其周長和面積,最後輸出周長和面積。
◆輸出浮點數到小數點後第二位。
'''
length=eval(input('請輸入矩形的長:'))
width=eval(input('請輸入矩形的寬:'))
print('周長 = {:.2f}'.format(2*(length+width)))
print('面積 = {:.2f}'.format(length*width))
