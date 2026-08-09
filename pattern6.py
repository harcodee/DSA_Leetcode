
def pattern6(n):
    for i in range(1 , n+1):
        for j in range(n-i):
            print(j,end="")
        print()
n = int(input())  
pattern6(n)