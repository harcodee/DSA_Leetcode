import math
class Solution:
    def getDivisors(self, n):
        # code here
        #optimal
        s = []
        for i in range(1, math.isqrt(n)+1):
            if n % i == 0:
                s.append(i)
                if i != n//i:
                    s.append(n//i)
        s.sort()
        return s
        
                
        