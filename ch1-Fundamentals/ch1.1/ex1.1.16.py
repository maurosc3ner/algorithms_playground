
def exR1(n):
    if(n<=0): return 0
    return exR1(n-3)+n+exR1(n-2)+n

print(exR1(6))


