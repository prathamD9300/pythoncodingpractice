def outputcount(n,arr):
    count = 0
    sum = 0
    for i in range(0,n):
        sum = sum + arr[i]
        if sum==0:
            count=count+1
    return count
        
n = int(input())
arr = list(map(int,input().split(' ')))
print(outputcount(n,arr))