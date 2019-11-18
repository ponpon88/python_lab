mystr = '帳號裡的餘額為：'
myMoney = 300

# 不同類型變數無法相加，如 mystr + myMoney
print(mystr + str(myMoney))
print(type(myMoney))

# 轉換型態，放置到另一變數
myMoney = str(myMoney)
print(type(myMoney))


socre = 78
name = "Pon Hsiao"
print("%s你的Pyhome成績是%d" % (name, socre))
# print("{s}你的Pyhome成績是{n}" % (name, socre))
# print("%s你的Pyhome成績是%d" % (name, socre))
s