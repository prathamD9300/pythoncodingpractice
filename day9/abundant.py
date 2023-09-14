a = int(input())
temp = a
f=[]
for i in range(1,temp):
    if temp%i==0:
        f.append(i)
sum = sum(f)
if a<sum:
    print("it is abund number")
else:
    print("not abundant number")