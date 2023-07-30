# rats problem
def sufffood(r,unit,arr,n):
    req = r*unit
    if n == 0:
        return -1
    foodavl = 0
    house = 0
    for house in range(n):
        foodavl = foodavl + arr[house]
        
        if foodavl >= req:
            break
        
    if req > foodavl:
        return 0
    return house +1
r = int(input())
unit = int(input())
n= int(input())
arr = list (map(int,input().split()))
print(sufffood(r,unit,arr,n))