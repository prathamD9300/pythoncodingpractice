a = input()
len = len(a)
b = int(a)
sum = 0
while b>0:
    digit = int(b%10)
    sum = sum + (digit**len)
    b = int(b/10)
if sum==int(a):
    print("armstrong")
else:
    print("not armstrong")
    
print(sum)
    
    