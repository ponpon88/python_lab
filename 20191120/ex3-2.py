""" value = 3
ans = 0
value = input('Please input your number(0~7):')
value = int(value)
if value == 1 or value == 3 or value == 5 or value == 7:
    ans += 1
if value == 2 or value == 3 or value == 6 or value == 7:
    ans += 2
if value == 4 or value == 5 or value == 6 or value == 7:
    ans += 4
print('Anser:%d' % ans) """

value = 0
ans = 0
value = input('if your number(1,3,5,7) return Y else N:')
if value == 'Y' or value == 'y':
    ans += 1
value = input('if your number(2,3,6,7) return Y else N:')
if value == 'Y' or value == 'y':
    ans += 2
value = input('if your number(4,5,6,7) return Y else N:')
if value == 'Y' or value == 'y':
    ans += 4

print('Anser:%d' % ans)
