a = int(input())
flag = 1
for i in range(2,a):
    if a%i==0:
        flag = 2
if flag == 2:
    print("not prime")
else:
    print("prime")