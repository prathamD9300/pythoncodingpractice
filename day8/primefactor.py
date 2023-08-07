n = int(input())
for i in range(2,n+1):
    a = n%i
    flag=0
    if a==0:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i,end=' ')
        