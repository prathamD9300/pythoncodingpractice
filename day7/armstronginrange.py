a = int(input())
b = int(input())
for i in range(a,b+1):
    order = len(str(i))
    temp=i
    sum = 0
    while temp>0:
        digit = int(temp%10)
        sum = sum + (digit**order)
        temp = int(temp/10)
    if sum==i:
        print(i,end=' ')



