word = {'A': 4,'E': 3,'G': 6 ,'I': 1, 'O': 0,'S':5 ,'Z': 2 }
myword = input("input:")
n = len(myword) 
for w in range(0,n):
    if myword[w] in word:
        print(word[myword[w]], end='')
    else:
        print(myword[w], end='')

