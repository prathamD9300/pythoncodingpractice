a = [5,43,56,7,8,76,54,12,34,321]
maxi = a[0]
mini = a[0]
for i in a:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print("max ele",maxi)
print("min ele",mini)