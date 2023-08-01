a = int(12345)
reverse = 0
while a>0:
    last = int(a%10)
    reverse = (reverse*10)+last
    a = int(a/10)
print(reverse)