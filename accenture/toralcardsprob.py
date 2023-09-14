def totalcards(n):
    if n==0:
        return 0
    if n==1:
        return 2
    
    total= (2*n)+(n-1)+totalcards(n-1)
    return total
n = int(input())
print(totalcards(n))