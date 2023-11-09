#if後面隱藏了bool函數，判斷True或是False，
#False只有4種情況：0, None, 空, False

#單向if
a = 100
b = 200
if a < b:
    print(a)
    
#雙向if
score = eval(input('Please enter your math score:'))
if score >= 60:
    print('Pass!')
else:
    print('Fighting!')
    
#多項if
score = eval(input('Please enter your math score:'))
if score >= 90:
    print('You got A!')
elif score >= 80:
    print('You got B!')
elif score >= 70:
    print('You got C!')
elif score >= 60:
    print('You got D!')
else:
    print('Fighting!')
    
#巢項if(Py冒號後面一定要縮排，巢狀結構閱讀不易)
score = eval(input('Please enter your math score:'))
if score >= 90:
    print('You got A!')
else:
    if score >= 80:
        print('You got B!')
    else:
        if score >= 70:
            print('You got C!')
        else:
            if score >= 60:
                print('You got D!')
            else:
                print('Fighting!')

