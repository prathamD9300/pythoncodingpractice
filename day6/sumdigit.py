a = int(input())
last = 0
sum = int(0)
while a>0:
    last=a%10
    sum = int(sum + last)
    a = a/10
print(sum)