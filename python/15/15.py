#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XV. 檔案讀取、寫入

#XV1. 開啟檔案
file = open("extraction.txt",mode = "r",encoding = "utf-8") #括號內第一項是開啟的檔案，第二項是開啟模式，第三項是編碼
#XV101. 檔案位置
#1. 絕對路徑: C:/Users/noob/noob/nuke.exe
#2. 相對路鸻: nuke.exe
#XV102. 開啟模式
#1. mode = "r" 讀取
#2. mode = "w" 覆寫
#3. mode = "a" 在原先的資料後加東西
print(file.read()) #開啟檔案 (欸好像開不到內)
file.close() #關掉檔案，以免佔用電腦資源
#XV103. 更多開啟檔案方式
print(file.readline()) #只讀取一行
print(file.readlines()) #把每行文字放到列表
file.write("Bruh") #覆寫(mode = "w")

#檔案可能開不到哦！