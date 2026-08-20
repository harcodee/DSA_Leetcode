'''
*****
****
***
**
*
'''


def pattern5(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()
n = int(input())  
pattern5(n)
