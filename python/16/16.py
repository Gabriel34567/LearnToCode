#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#模組
import extraction #這是自己寫的模組
import time #這是內建的

#XVI. 模組 MODULE

#把另一個py檔案的函式和變數引入到這個檔案

#用Python內建模組

x = 0

def count10s():
    while x > 10:
        time.sleep(1) #模組
        print(x + "sec")

count10s()

#用自己寫的模組

extraction.extractNum()

#Python所有內建模組: https://docs.python.org/3.10/py-modindex.html

#當然還有第三方的模組，要下載才可以使用，或者在終端機使用 pip install (模組名稱)