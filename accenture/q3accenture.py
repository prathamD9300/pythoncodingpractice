def CheckPassword(s,n):
    if n<4:
        return 0
    if s[0].isdigit():
        return 0
    cap = 0
    num = 0
    for i in range(n):
        if s[i]==' ' or s[i]=='/':
            return 0
        if s[i]>='A' and s[i]<='Z':
            cap=cap+1
        elif s[i].isdigit:
            num = num+1
        
        
    if cap >=1 and num >=1:
        return 1
    else:
        return 0
s=input()
a = len(s)
print(CheckPassword(s,a))