"""
練習一
設計一程式, 接受鍵盤輸入數字, 每10分一個等級, 回應ABCDE等級
滿分100分,最低0分
"""
print('轉換成績等級')
score = input('請輸入 0~100 分:')
sc = int(score)
if sc <= 100 and sc >= 90:
    print("A")
elif sc < 90 and sc >= 80:
    print("B")
elif sc < 80 and sc >= 70:
    print("C")
elif sc < 70 and sc >= 60:
    print("D")
elif sc < 60 and sc >= 0:
    print("E")
else:
    print("Error")
