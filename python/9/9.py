#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#IX. 建立進階計算機

#如何讓計算機可以計算加、減、乘、除？
val1 = input("INPUT A VALUE ")
sym = input("INPUT CALCULATION (+ or - or * or /)") #新增一個變數：輸入運算符號
val2 = input("INPUT ANOHTER VALUE ")
if sym == "+": #使用if來判斷運算符號
    print(float(val1) + float(val2))
elif sym == "-":
    print(float(val1) - float(val2))
elif sym == "*":
    print(float(val1) * float(val2))
elif sym == "/":
    print(float(val1) / float(val2))
else:
    print("ERROR")