import math
a = [3,4,2,6,7,8,50]
mini = math.inf
second = math.inf
for i in range(len(a)):
    if a[i]<mini:
        mini = a[i]
for i in range(len(a)):
    if a[i]<second and a[i]!=mini:
        second=a[i]
print(second)