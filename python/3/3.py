#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#模組
from math import ceil, floor, sqrt

#III. 數字 NUMBER

#III1. 數字的基本類型
#III101. 正整數
print(69)
#III102. 小數
print(420.69)
#III103. 負數
print(-69)

#III2. 四則運算
#III201. 加法(+)
print(420+69)
#III202. 減法(-)
print(420-69)
#III203. 乘法(*)
print(420*69)
#III204A. 除法(/)
print(420/69)
#III204B. 除法(只保留整數部分)(//)
print(420//69)
#III204C. 除法(只保留餘數部分)(%)
print(420%69)
#在Python中，可以進行連續的運算，而且有先乘除後加減的規則哦！
#例如
print(69+4*20)

#III3. 四則運算(有括號)
#在Python中，也有先計算括號內的規則哦！
#例如
print((69+4)*20)

#III4. 代入變數
value = 69420
print(value+2)

#III5. 函式
#III501. 使數字變成字串(str)
print(str(value)) #由於字串不能與數字相連，所以要把數字變成字串才能與其他字串相連
print("Meme number is... " + str(value))
#III502. 絕對值(abs)
iii502 = -value
print(abs(iii502))
#III503. 次方(pow)
iii5031 = 69
iii5032 = 2
print(pow(iii5031,iii5032)) #括號內的第一項是底數，第二項是指數/次方
#III504. 找出最大的值(max)
print(max(6,9,4,2,0,69,42,420,69420,49620,42069,69042))
#注意事項
#1. 所有項都只能是數字或變數
#2. 括號內項數不限
#3. 括號內的項不用由高至低或由低至高排序
#III504. 找出最小的值(min)
print(min(6,9,4,2,0,69,42,420,69420,49620,42069,69042))
#注意事項
#1. 所有項都只能是數字或變數
#2. 括號內項數不限
#3. 括號內的項不用由高至低或由低至高排序
#III505. 四捨五入(round)
iii505 = 6.9
print(round(iii505))
#III506. 無條件捨去(floor)
iii506 = 6.9
print(floor(iii506))
#III507. 無條件進位
iii507 = 6.9
print(ceil(iii507))
#III508. 開根號
iii508 = 4761
print(sqrt(iii508))