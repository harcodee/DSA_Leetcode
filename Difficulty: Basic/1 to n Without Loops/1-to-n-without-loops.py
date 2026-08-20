class Solution:
    def printTillN(self, n):
    	#code here 
    	def num(i):
    	    if i > n:
    	        return
    	    print(i,end = ' ')
    	    num(i+1)
        num(1) 