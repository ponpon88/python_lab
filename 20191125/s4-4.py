scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:
        continue
    games += 1
print("More than 30:%d" % games)

print(scores[3:6])
print("前3場分數", end='')
print(scores[:3])
print("從尾巴扣2場分數", end='')
print(scores[:-2])
print("取得最後1場分數", end='')
print(scores[-1])
print("取得倒屬第2場分數", end='')
print(scores[-2])
