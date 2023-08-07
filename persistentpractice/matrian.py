def secretket(sc,f,s):
    return pow(pow(sc,f,10),s,1000000007)
print(secretket(3,1000000007,4))