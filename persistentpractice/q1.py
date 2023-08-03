# n=list(map(int,input().split()))
# n.sort()
# print(n)
a = [3,2,5,67,8,9,56]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp = a[j]
            a[j]=a[i]
            a[i]=temp
print(a)