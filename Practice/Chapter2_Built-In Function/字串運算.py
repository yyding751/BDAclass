#連接運算子+
print('Happy'+'Birthday'+'to'+'小美')

#重複運算子*(限正整數)
print(3*'XYZ')
print('XYZ'*3)
print(-3*'XYZ')
print(0*'XYZ')

#比較運算子(參考Ascii code)
print('X'>'A')
print('123'>'456')
print('XYZ'>'xyz')

#in/not in運算子
print('or' in 'forever')
print('for'  not in 'forever')

#索引運算子
S='Python程式設計'
print(S[0])
print(S[-10])
print(S[9])
print(S[-1])

#片段運算子
'''
!!!包前不包後!!!
正索引(從左邊數起)從0
副索引(從右邊數起)從-1
start/end可省略不打
'''
S='Python程式設計'
print(S[2:5])
print(S[3:8])
print(S[5:-1])
print(S[:2])
print(S[2:])

#Exercise
S1 = 'HappyNewYear'
S2 = 'happynewyear'
S3 = 'new'
'''
E1. S1與S2是否相等
E2. S3是否從在於S1
E3. S1的第5~9個字元
'''
'''ANSWER'''
print(S1==S2)
print(S3 in S1)
print(S1[4:9])
