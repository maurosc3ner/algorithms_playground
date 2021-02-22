def misterio(a,b):
    if (b==0): 
        return 0
    if (b%2==0): 
        return misterio(a+a,b/2)
    return misterio(a+a,b/2)+a

def misterio2(a,b):
    if (b==0): 
        return 1
    if (b%2==0): 
        return misterio2(a*a,b/2)
    return misterio(a*a,b/2)*a

final=misterio(2,25)
print(final)
# no da
# print(misterio2(2,25))