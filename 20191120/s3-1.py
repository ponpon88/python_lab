name = input('Please input your name:')
score = input('Please input python score:')

print(type(name))
print(type(score))

numstr = input("Please your fumela:")
number = eval(numstr)
print("result: %6.3f" % number)

n1, n2, n3 = eval(input("請輸入3個數字(需要用逗號分隔):"))

average = (n1 + n2 + n3)/3
print("3個數字的平均: %6.2f" % average)
