# a = '123'
# b = a[::-1]
# if a==b:
#     print("palindrome")
# else:
#     print("not")
a = 12321
temp = a
reverse = 0
last = 0
while temp>0:
    last = int(temp%10)
    reverse = (reverse*10)+last
    temp = int(temp/10)
print(reverse)
if a == reverse:
    print("palinedroe")
else:
    print("not a palindrome")
