#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XIII. for 迴圈

#XIII1. 表示方法
xiii1str = "Meme" #字串
xiii1list = [6,9,4,2,0] #列表
#XIII101. in 字串
for xiii101 in xiii1str:
    print(xiii101)
#XIII102. in 列表
for xiii102 in xiii1list:
    print(xiii102)

#for迴圈就是把in後面的值分成多個小單位後把它們代入到變數中
#每個小單位的值都會被代入到變數中再運行程式碼
#字串的小單位是字母
#列表的單小位是值

#XIII2. 其他用法
#XIII201A. in range (到某個數為止)
for xiii201 in range(69): #括號內填數字
    print(xiii201) #結果：從0一直運行到括號內的數字的前一位為止
#XIII201B. in range (從一個數到另外一個數)
for xiii202 in range(6,9): #括號內的兩項都填數字
    print(xiii202) #結果：從括號內第一項的數字一直運行到第二項數字的前一位為止