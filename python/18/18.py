#Python教學 (初學者入門)
#影片(不是我的！)：https://www.youtube.com/watch?v=zdMUJJKFdsU
#如果要清除終端機的所有指令，用cls(Windows) / clear(Mac) 清除指令

#XVIII. Q&A 程式

#模組
from questions import question

#問題
test = [
    "NICE Number is... \nA. 67 \nB. 69 \nC. 87 \nD. 99",
    "What is 9+10? \nA. 20 \nB. 21 \nC. 22 \nD. 23",
    "How to respond when someone said\"Fantastic\"? \nA. Fantastic \nB. Noob \nC. Cocacolastic \nD. Music"
]

questions = [
    question(test[0],"B"),
    question(test[1],"B"),
    question(test[2],"C")
]

def commence(questions):
    points = 0
    for question in questions:
        answer = input(question.desc)
        if answer == question.correctAnswer:
            points += 2
    print("Result: " + str(points))

commence(questions)