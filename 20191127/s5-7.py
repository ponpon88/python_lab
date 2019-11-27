def interest(interest_type, subject='日本'):
    print("我的興趣是" + interest_type)
    print("在 " + interest_type + '中,最喜愛' + subject)
    print()


interest('b')
interest('b', 'a')
interest(subject='b', interest_type='a')


def subtract(x1, x2):
    result = x1 - x2
    return result


print("a-b:")
a = int(input("a = "))
b = int(input("b = "))

print("a-b:", subtract(a, b))
