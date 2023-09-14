n = int(input())
count = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            if a**2+b**2+c**2+a*b+b*c+c*a==n:
                count = count+1
print(count)