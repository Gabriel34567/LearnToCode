#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XVII. 類別 CLASS 、 物件 OBJECT

#回顧：Python有哪些資料型態？
#A. 基本型態
num = 69 #數字
str = "Meme" #字串
tf = True #布林值
#B. 延伸
li = [69,"Meme",True] #列表
tup = (69,"Meme",True) #元組
dictionary = {"數字":"Number","字串":"String","列表":"List","元組":"Tuple"} #字典

#某些事物不能只使用上述的資料型態去描述，所以需要用到類別

#XVII1. 自定義類別 (以MM2為例)
#1. 創建類別
class character:
    def __init__(self,way_to_win,bonus):
        self.way_to_win = way_to_win
        self.bonus = bonus
#2. 創建資料
innocent = character("Survive until victory","Become a hero")
sheriff = character("Hunt down the murderer","Innocents saved")
murderer = character("Eliminate everyone",None)
#這些都被稱為物件

#XVII2. 擷取物件信息
print(innocent.way_to_win) #前者是物件名稱，後者是資料