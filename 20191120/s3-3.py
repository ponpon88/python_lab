"""
迴圈
"""
""" for x in range(0, 3):
    print(x)
    print("a")

for x in range(10, 0, -2):
    print(x)

for x in range(1, 10):
    for y in range(1, 10):
        total = x*y
        print('%d * %d = %d ' % (x, y, total)) """

for x in range(1, 10):
    for y in range(1, x+1):
        print("*", end='')
    print("")
