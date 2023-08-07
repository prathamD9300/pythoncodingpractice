n = int(input())
power = int(input())
apower = n
for i in range(1,power):
    if power == 0:
        print("1")
    elif power==1:
        print(n)
    else:
        apower= apower*n
print(apower)