class Solution:
    def gcd(self, a, b):
        # code here
        #OPTIMAL - EUCLIDEAN FORMULA
        while a > 0 and b > 0:
            if a>b:
                a = a%b
            else:
                b = b%a
                
        if a == 0:
            return b
        return a
        