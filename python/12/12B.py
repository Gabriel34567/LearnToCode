#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XII. 猜數字遊戲

#XII2. 增加挑戰性--限制猜測次數
#XII201. 變數

objective = 69 #這是目標數字！
estimation = None #這是用於接收用戶的猜測的變數，初始值為"None"
chances = 5 #限制猜測次數
chancesUsed = 0 #已猜測的次數
defeated = False #是否遊戲失敗
#XII202. 運行代碼
while estimation != objective and not(defeated):
    if chancesUsed < chances:
        estimation = int(input("INPUT A NUMBER"))
        if estimation > objective:
            chancesUsed += 1
            print("SIKE! THAT'S THE WRONG NUMBER! (TOO BIG) " + str(chances - chancesUsed) + " chances left")
        elif estimation < objective:
            chancesUsed += 1
            print("SIKE! THAT'S THE WRONG NUMBER! (TOO SMALL) " + str (chances - chancesUsed) + " chances left")
    else:
        defeated = True
if defeated:
    print("Defeat...")
    print("The number was " + str(objective))
else:
    print("VICTORY!")
    print("You made it in " + str(chancesUsed) + " round(s)!")