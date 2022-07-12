#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#VIII. if 判斷句

#VIII1. 例子
#例如：
#VIII101. 情景一、普通判斷
#見到老六(條件)
#直接跟他剛(發生的事)
#用Python表示如下
viii101 = True #變數
if viii101: #條件
    print("直接跟他剛") #發生的事
#VIII102. 情景二、普通判斷 + 否則
#見到老六(條件)
#直接跟他剛(發生的事)
#否則，苟分就好(否則發生的事)
#用Python表示如下
viii102 = False #變數
if viii102:
    print("直接跟他剛")
else:
    print("苟分就好")
#VIII103. 情景三、多重判斷
#分數100+，評等A+(條件及發生的事)
#分數90+，評等A(條件及發生的事)
#分數80+，評等B(條件及發生的事)
#分數70+，評等C(條件及發生的事)
#分數60+，評等D(條件及發生的事)
#分數0+，評等F(條件及發生的事)
#否則，無評等！
#用Python表示如下
viii103 = 69
if viii103==100: #條件
    print("評等A+") #發生的事
elif viii103>=90:
    print("評等A")
elif viii103>=80:
    print("評等B")
elif viii103>=70:
    print("評等C")
elif viii103>=60:
    print("評等D")
elif viii103>=0:
    print("評等F")
else:
    print("三小啦！")
#VIII104. 情景四、並列條件
#如果有多於69發子彈且對面是老六(並列條件)
#直接剛！(發生的事)
#否則，苟分就算了(否則發生的事)
#用Python表示如下
viii104Force = 69
viii104OldVI = True
if viii104Force >=420 and  viii104OldVI:
    print("直接剛！")
else:
    print("苟分就好了")
#VIII105. 情景五、任選一個條件
#如果有多於69發子彈且對面是老六(並列條件)
#直接剛！(發生的事)
#否則，苟分就算了(否則發生的事)
#用Python表示如下
#變數在情景四
if viii104Force >=420 or viii104OldVI:
    print("直接剛！")
else:
    print("苟分就好了")
#VIII106. 情景六、False條件
#如果今天天氣不好
#做個老六
#否則，做個老八
#用Python表示如下
viii106Clear = False
if not(viii106Clear):
    print("做個老六")
else:
    print("做個老八")