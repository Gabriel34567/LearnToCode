#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#模組
from bot import bot

#XX. 繼承 INHERIANCE

#有兩個類別，請查看bot.py及hero.py

#不難發現，bot跟hero有3個共同的資料

#我們可以用bot的類別去繼承hero這個類別(即把bot類別的資料拷到hero類別)

#hero這個類別可以這樣寫

class hero(bot):
    def __init__(self, agility, defense, offense,HP):
        self.agility = agility
        self.defense = defense
        self.offense = offense
        self.HP = HP
    
    #此處可以省略大量函式，因為已經繼承bot的函式
    def print_HP(self):
        print(self.HP)

heroA = hero(6,9,4,20)

#使用自己寫的函式
heroA.print_HP()

#也可以使用bot繼承的函式
heroA.print_agility()