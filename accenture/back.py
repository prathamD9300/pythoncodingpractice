t = int(input())
n = int(input())
for i in range(n):
    a = int(input())
    b = {}
    if a in b:
        b[a] = b[a]+1
    else:
        b[a]=1
for j in b:
    if b[j]==1:
        print(j)