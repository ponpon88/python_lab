a = {'one': 11, 'two': 2}
a1 = a.copy()
a.clear()
print(a)
print(a1)

print(a1.items())
print(a1.keys())
print(a1.values())

a2 = {'one': 10, 'two': 777}
a1.update(a1)
print(len(a1))
print(max(a1))
print(min(a1))
