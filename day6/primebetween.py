low = int(input())
high = int(input())
prime=[]

for i in range(low,high+1):
    flag = 1
    if i <2:
        continue
    if i ==2:
        prime.append(i)
        continue
    for j in range(2,i):
        if i%j==0:
            flag = 2
            break
    if flag == 1:
        prime.append(i)
print(prime)
    
            