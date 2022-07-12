#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#IV. 建立基本計算機

#IV1. 輸入
sheriff = input("Input a sheriff ") #儲存用戶輸入資料
murderer = input("Input a murderer ") #儲存用戶輸入資料
print("The sheriff " + sheriff + " killed the murderer " + murderer) #結果
#注意事項：無論用戶輸入什麼，Python都會把它們當作字串

#IV2. 讓字串變成數字
#IV201. 僅限整數
iv2011 = input("INPUT A NUMBER")
iv2012 = input("INPUT ANOTHER NUMBER")
print(int(iv2011) + int(iv2012))
#注意事項：只能輸入整數，不能輸入小數或非數字
#IV202. 所有數字
iv2021 = input("INPUT A VALUE")
iv2022 = input("INPUT ANOTHER VALUE")
print(float(iv2021) + float(iv2022))
#注意事項：只能輸入數字