def revers(zoro):
    zoro.reverse()
    x=" ".join(zoro)
    
    return x
    
        
str=input().split()
x=revers(str)
print(x)