h = float(input())
w = float(input())
h1 =float(input())
w1 = float(input())
ch=0
while h1!=h:
    if h1<=h/2 and h!=h1:
        h = h-2
        ch = ch+1
    elif h1>h/2 and h!=h1:
        h = h/2
        ch = ch+1
while w1!=w:
    if w1<=w/2 and w!=w1:
        w = w/2
        ch = ch+1
    elif w1>w/2 and w!=w1:
        w = w-1
        ch = ch+1
print(ch)
    
