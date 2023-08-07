a=145
arr = [1,4,5]
sum = 0
for i in range(0,(len(arr))):
    fact=1
    b = arr[i]
    for j in range(1,b+1):
        fact = fact*j
    sum = sum+fact
if sum==a:
    print("its strong no")
            