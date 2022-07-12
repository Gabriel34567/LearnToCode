#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XIX. 物件函式

#創建類別
class bot:
    def __init__(self,agility,defense,offense):
        self.agility = agility
        self.defense = defense
        self.offense = offense
    
    def print_agility(self): #記得要在class內創建此函式，括號內是self
        return self.agility

#創建物件
botA = bot(6.9,69,420)

#呼叫函式
print(botA.print_agility()) #第一項是物件名稱，第二項是函式名稱，不忘再加個小括號