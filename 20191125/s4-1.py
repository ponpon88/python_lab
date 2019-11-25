scores = [33, 22, 41, 25, 39, 43, 27, 38, 40, 39]
games = 0
for score in scores:
    if score < 30:
        continue
    games += 1
print("More than 30:%d" % games)

# 取得 list 最大值
print("Max:%d" % max(scores))

# 取得 list 最小值
print("Min:%d" % min(scores))

# count list 中某一個值出現的次數
print("count:%d" % scores.count(39))
