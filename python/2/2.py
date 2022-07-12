#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#II. 字串

#II1. 字串表示方法
print("Yes, UA!")

#II2. 其他字串種類
#II201. 換行 (\n)
print("Yes! \nUA!")
#II202. 雙引號 (\")
print("Yes, \"UA!\"")
#II203. 字串相連
print("Yes" + "UA!")
#II204. 使用變數
phrase1 = "Yes"
phrase2 = "UA!"
print(phrase1 + phrase2)

#II3. 字串函式
sentence = "Yes, UA!"
#II301. 全部小寫
print(sentence.lower())
#II302. 全部大寫
print(sentence.upper())
#II303. 判斷字串裏的所有字母是否都是大寫
ii303 = "YES, UA!"
print(ii303.isupper()) #只有在所有字母都是大寫的時候，回傳值才會是True
print(sentence.isupper()) #否則回傳值為False
#II304. 判斷字串裏的所有字母是否都是小寫
ii304 = "yes, ua!"
print(ii304.islower()) #只有在所有字母都是小寫的時候，回傳值才會是True
print(sentence.islower()) #否則回傳值為False

#II4. 以字串的位置找到字母
#II401. 一個字母
print(sentence[0]) #中括號內的數字是指字串的位置
#注意事項
#1. 中括號內只能填數字
#2. 字串的第一位的數值是0，第二位是1，第三位是2，如此類推
#II402A. 多個字母(指定範圍)
print(sentence[0:3])
#注意事項
#1. 中括號內只能填數字
#2. 字串的第一位的數值是0，第二位是1，第三位是2，如此類推
#3. 兩個數值中間用":"表示，例如6:9表示第6~8個字母(後面的數值記得要加1)
#II402B. 多個字母(在某字母之前)
print(sentence[:3])
#注意事項
#1. 中括號內只能填數字
#2. 字串的第一位的數值是0，第二位是1，第三位是2，如此類推
#3. 在數值前加":"，例如:9表示第8個字母之前(數值記得要加1)
#II402C. 多個字母(在某字母之後)
print(sentence[5:])
#注意事項
#1. 中括號內只能填數字
#2. 字串的第一位的數值是0，第二位是1，第三位是2，如此類推
#3. 在數值後加":"，例如6:表示第6個字母之後

#II5. 字母在字串的位置
print(sentence.index("Y")) #用途：從字串中找到該字母的位置
#注意事項
#1. 括號內只能填字串中的字母，其他字母視為無效
#2. 回傳值的第一位的數值是0，第二位是1，第三位是2，如此類推
#3. 如果字串內有重複的字母，只會回傳最前一位的值

#II6. 替換
print(sentence.replace("Yes","No")) #用途：替換字串中的某些字母
#注意事項
#1. 括號內第一個要填的是字串中要替換的字母，第二個要填的是替代該字母的東西
#2. 如果字串內有重複的字母，所有被選中的字母也會被替代