#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XI. while 迴圈
#讓程式碼忙得不停轉！

#XI1. while的用法
xi = 69
while xi<=420: #當這個條件成立時會不斷重複代碼直到條件不成立
    print(xi)
    xi = xi+3 #*1
print("結束！") #這段程式碼會在上述條件成立時執行

#*1補充：這段也可以表達為
xi += 3