#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#I. 基本資料型態 & 變數

#I1. 基本資料型態
#I101. 字串
"共三小"
"SB"
#I102. 數字
69
420
69.420
#I103. 布林值 (是/否)
True
False

#I2. 變數
#I201. 變數類型
value1 = "傻逼" #字串(不可忽略"")
value2 = 69420 #數值
value3 = True #布林值
#I202. 注意事項
#1. 變數名稱只能是英文、數字或_組合
#2. 變數開頭不能為數字

#I3. 變數的用途
#使用print指令打印文字 (不是物理性打印哦)
#STEP 1. 原有的句子
print("名稱:傻逼")
print("傻逼是一個大聰明")
#STEP 2. 創建變數
name = "傻逼"
#STEP 3. 把變數代入至原有的句子中
print("名稱:" + name)
print(name + "是一個大聰明")
#這樣不用一行一行去改哦！(方便！)

#I4. 重名變數？
print(name)
name = "SB"
print(name)
name = "NB"
print(name)
name = 2
print(name)
name = False
print(name)
#變數重名後，原本的數據會被下面的數據取代
#可以是字串、數字或布林值