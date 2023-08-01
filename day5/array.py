a = [1,2,2,3,4]
b = []
sum = 0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            break
        j = j+1
    if j==len(a):
        sum = sum+a[i]
        b.append(a[i])
print(sum)
print(b)