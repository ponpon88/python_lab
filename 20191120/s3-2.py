"""
if的練習
"""
x = 5
y = 3
if x > y:
    print("X > Y")
    print('這是在if區塊的程式碼')

print('這一行不管判斷是否成立都會輸出')

x = 1
y = 3
if x > y:
    print("X > Y")
else:
    print("X <= Y")

if x > y:
    print("X > Y")
elif x == y:
    print("X == Y")
else:
    print("X < Y")
