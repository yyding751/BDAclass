#輸出至檔案
##若未設定路徑，檔案會存在跟該PY檔相同路徑
text = '''將內容存到txt
1.A
2.B
3.C'''
print(text, file = open(r'C:\Users\student\Desktop\BDA Class\BDA Class\Python\Course Material\data.txt', 'w'))

#%%
#清空並寫入檔案
##write()內容須為str

file = open(r'C:\Users\student\Desktop\writedata.txt','w')
file.write('寫入資料到檔案\n')
file.write('ABC\n')
file.write('123')
file.close()
#檔案已存在、新增內容在尾端
import random
file = open(r'C:\Users\student\Desktop\writedata.txt','a')
for i in range(10):
    file.write(str(random.randint(1,100))+'\n')
file.close()

#讀取檔案
#####預設為'r'
file = open(r'C:\Users\student\Desktop\writedata.txt','r')
context = file.read()
print(context)
file.close()

#%%
#改寫w：with敘述：將存取檔案的動作包裝在一個區塊，執行完會自動關閉檔案
with open(r'C:\Users\student\Desktop\writedata.txt','w') as file:
    file.write('寫入資料到檔案\n')
    file.write('ABC\n')
    file.write('123')



#%%
#產生特定個數的特定範圍內亂數
###randint包前也包後
import random
for i in range(10):
    print(random.randint(1,100))
    
    
    
    
    