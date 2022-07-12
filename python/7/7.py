#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#VII. 函式 FUNCTION

#VII1. 自定義函式
#VII101. 普通函式
#第一步. 定義函式
def vii101(): #定義函式名稱
    print("MEMES NEVER DIE!") #函式內部
#第二步. 呼叫函式
vii101() #在函式後要加一對括號
#VII102. 輸入資料
#第一步. 定義函式
def vii102(memeA,memeB):
    print("YOUR FAVORITE MEMES ARE... " + memeA + " AND " + memeB)
#第二步. 呼叫函式
vii102("69","420") #括號內的值對應着自定義函式的兩個值，括號內只能是字串
#VII103A. return
#函式內部只要有return，呼叫的值也將會被return的值代替
def vii103a():
    print("LOL")
    return "LMAO" #return的用途是為了對數值做更多的運算
print(vii103a())
#VII103B. return 補充
#return之後的代碼都不會被運行
def vii103b():
    print(5+5)
    return 6
    print ("sus") #不能被執行
print(vii103b())