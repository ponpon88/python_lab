weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
for n in range(6, -1, -1):
    print(weekday[n])

print(weekday[::])
print(weekday[::-1])
weekday.reverse()
print(weekday)
weekday.sort()
print(weekday)

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

del weekday[3:5]
print(weekday)

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
weekday[3:4] = '4'
print(weekday)

# 插入兩個值
weekday[4:5] = 'thu', 'tue'
print(weekday)
print(weekday.index('thu'))

# len 取得 list 長度
print(len(weekday))

# 
