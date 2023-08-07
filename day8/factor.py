n = int(input())
a = 1
for i in range(1,n+1):
    a = n%i
    if a==0:
        print(i,end=' ')