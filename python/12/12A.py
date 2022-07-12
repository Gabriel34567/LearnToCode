#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XII. 猜數字遊戲
#這個遊戲需用到while及if

#遊戲規則：
#在範圍內任意輸入一個數字
#系統會根據你輸入的數字及目標數字而給予提示 (太大了/太小了)
#猜到目標數字，遊戲勝利

#XII1. 基礎代碼：
#XII101. 變數
objective = 69 #這是目標數字！
estimation = None #這是用於接收用戶的猜測的變數，初始值為"None"
#XII102. 運行代碼
while estimation != objective:
    estimation = int(input("INPUT A NUMBER"))
    if estimation > objective:
        print("SIKE! THAT'S THE WRONG NUMBER! (TOO BIG)")
    elif estimation < objective:
        print("SIKE! THAT'S THE WRONG NUMBER! (TOO SMALL)")
print("VICTORY!")

#想加點挑戰性？詳見檔案12B.py