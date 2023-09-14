n = int(input())
for i in range(0,n):
    for k in range (0,i):
        print(" 1",end='')
    for i in range(i,n):
        print('* ',end='')
    print()