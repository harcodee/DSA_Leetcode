n = int(input())

# Code here
def gfg(count,n):
    if count == n:
        return
    print("GFG",end =' ')
    count +=1
    gfg(count, n)
    
gfg(0,n)
    
    
