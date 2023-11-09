#基本字串函式
'''ord(x)傳回字元參數x的unicode(d十進位)'''
print(ord('A'))
print(ord('€'))

'''chr(y)傳回整數參數x代表的unicode字元'''
print(chr(88))
print(chr(8364))

print(len('Python程式設計'))

print(min('Python程式設計'))
print(min('python程式設計'))

'''str(x)傳回數值參數x轉換成字串的結果'''
print(str(111.2))

#字串轉換函式(有3種方法)
X='Good Afternoon! How are you?'
print(X.upper())
print(X.lower())
print(X.capitalize())
print(X.title())
print(X.swapcase())
print(X.replace('oo','xx'))
print(X)

X=X.swapcase()
print(X)

#字串測試函式(有is, 會回傳布林值)
print(str.isupper('abcde'))
print(str.islower('abcde'))
'''isidentifier(s)字串s式合法的識別字(命名、含關鍵字)'''
print(str.isidentifier('a1bcde'))
print(str.isidentifier('1abcde'))

'''isspace所有字元皆為空白'''
print(str.isspace('  a  '))
print(str.isspace('     '))
print(str.istitle('It Is Ok'))

print('ABCDE'.isalpha())
print('abced'.isalpha())
print(''.isdigit())

print(''.isdecimal())

print(''.isnumeric())

#搜尋子字串函式
Y='HiHiHiHiHi'
print(Y.count('Hi'))
print(Y.startswith('HiH'))
print(Y.endswith('HiH'))
print(Y.endswith('iHi'))
print(Y.find('iHi'))
print(Y.rfind('iHi'))

#字串切割 str.split([chars])
X='1 3 5 4 7'
Y=X.split()
print(Y)
X='1,3,5,4,7'
Y=X.split(':')
print(Y)

#刪除指定的字元或空白函式 兩側
print('   abc   '.strip())
print('abcaespad ef'.strip('abcdef'))
print('aespa.com'.lstrip('acome'))
print('aespa.com'.rstrip('acome'))

#格式化函式
X='Hello Python'
print(X.center(20))
print(X.ljust(20))
print(X.rjust(20))
print(X.zfill(6))
print(X.zfill(20))
