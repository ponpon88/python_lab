x = y = 10
z = 10
print(id(x))
print(id(y))
print(id(z))
a = "test"
b = "python"
print(a, x)  # print 可以一次輸出多個值
print(type(x))
print(type(a))
print(type(y), type(b))

# 第1種單行程式折行的寫法

a1 = b1 = c1 = 10
x1 = a1 +\
    b1 +\
    c1 +\
    22
print(x1)

# 折行方式2
a2 = b2 = c2 = 12
x2 = (a2 +    # 可以用註解的折行
      b2 +
      c2 +
      77)
print(x2)

x3 = 'my var str'
print(x3)
del(x3)
print(x3)
