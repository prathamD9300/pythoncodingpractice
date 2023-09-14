def swapstr(str):
    n = len(str)
    first = str[:int(n/2)]
    second = str[-int((n/2)):]
    
    return second+first
str = 'prathamd'
str = swapstr(str)
print(str)