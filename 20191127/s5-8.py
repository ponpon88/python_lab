def mutifunction(x1, x2):
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2

    return addresult, subresult, mulresult, divresult


print("a-b:")
a = int(input("a = "))
b = int(input("b = "))
add, sub, mul, div = mutifunction(a, b)
print("a+b:", add)
print("a-b:", sub)
print("a*b:", mul)
print("a/b:", div)
