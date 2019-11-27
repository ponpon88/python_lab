def greeting(name):
    print("Hi, " + name + ' welcome')


def subtract(x1, x2):
    result = x1 - x2
    return(result)


# 以下可稱為主程式進入點
greeting('Pon')
a = int(input("a="))
b = int(input("b="))
print("a -b = ", end='')
print(subtract(a, b))
res = subtract(a, b)
print(res)
