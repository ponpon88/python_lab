def printmsg():
    print("副程式", msg)


''' Main func '''
msg = 'Global Variable'
print("主程式", msg)
printmsg()


def printmsg2():
    msg2 = "Local Variable"
    print("副程式", msg2)


''' Main func '''
msg2 = 'Global Variable'
print("主程式", msg2)
printmsg2()


def printmsg3():
    global msg3
    msg3 = "Local Variable"
    print("副程式", msg3)


''' Main func '''
msg3 = 'Global Variable'
print("主程式", msg3)
printmsg3()
print("主程式", msg3)
