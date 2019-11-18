
# 字串相加
str1 = "Pon Hsiao"
str2 = ' Pytho class day2'
str3 = str1 + str2
print(str3)

# 多行的方式
str4 = '''第1行文字加上 enter 段行
第2行
第3行
第4行
'''
print(str4)

# 因為沒有實質的終端機換行符號, 所以輸出果不會斷行，僅在程式碼中有段行顯示效果
str5 = '''第1行 斷行用\
第2行\
第3行\
'''
print(str5)

# 找尋字串中的字元
str6 = 'python'
print('p' in str6)
print('on' in str6)

# 求得字串長度
print(len(str5))

# 換行有被算入
print(len(str4))

print(str6 * 5)
str7 = " "
print(str7 * 20, str6)

# 印出字串中某一個字元
print(str6[0])
# 擷取部分字串，部分擷取時，只算頭，不算尾
print(str6[3:5])
# 擷取部分字串的位置到結尾
print(str6[3:])
# 擷取從頭到第3個的字元
print(str6[:4])
