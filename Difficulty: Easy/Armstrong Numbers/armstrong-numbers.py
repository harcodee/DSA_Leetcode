class Solution:
    def armstrongNumber (self, n):
        # code here 
        length = len(str(n))
        sum = 0
        num = n
        
        while n >0:
            ld = n%10
            sum += ld ** length
            n = n//10
            
        return sum == num
            
        