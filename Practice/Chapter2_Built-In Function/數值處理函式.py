print(abs(-100))
print(pow(2,5))
print(pow(8,2))
print(divmod(100,8))

print(min(1,3,False))
print(max(-3,-5,True))

print(bin(100))
print(oct(100))
print(hex(100))

print(int(666.666))
print(int('666'))
print(int('666.666')) !!!

print(float(666))
print(float("666"))

print(round(123.123))
print(round(123.123,2))
print(round(-123.123))
print(round(-123.123,2))
print(round(-123.127,2))

#小數一位且為0.5時，奇進偶不進，負數反之
print(round(5.5))
print(round(6.5))
print(round(-5.5))
print(round(-6.5))
#小數二位以上無準則可循

#math模組需先import math

#random模組需先import ramdom
import random
num = random.randint(1,3)
print(num)

print(format(123,'!^10'))
print(format(12356789,','))
print(format(123.456,'10.2f'))
print(format(123.456,'<10.2f'))