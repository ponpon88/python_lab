def factorial(n):
    if n == 1:
        return n
    else:
        return (n * factorial(n-1))


value = 3
print("3! = ", factorial(value))
value = 10
print("10! = ", factorial(value))

n = int(input("n ="))
print(n, "! = ", factorial(n))
