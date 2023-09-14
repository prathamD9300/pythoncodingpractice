def sumofdivisor(n):
    f=[]
    for i in range(1,n):
        if n%i==0:
            f.append(i)
    return sum(f)
a,b=map(int,input().split(' '))
if a/sumofdivisor(a)==b/sumofdivisor(b):
    print("friendly pair")