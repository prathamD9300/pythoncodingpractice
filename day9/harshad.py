a = int(input())
temp = a
sum = 0
while(temp>0):
    digit = int(temp%10)
    sum = sum + digit
    temp = temp/10
if a%sum==0:
    print("harshad number")
else:
    print("not a harshad")