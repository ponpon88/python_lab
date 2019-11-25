num = int(input("Input > 1 整數的質數:"))
if num == 2:
    print("%d是質數:" % num)
else:
    for n in range(2, num):
        if num % n == 0:
            print("%d不是質數:" % num)
            break
    else:
        print("%d是質數:" % num)
