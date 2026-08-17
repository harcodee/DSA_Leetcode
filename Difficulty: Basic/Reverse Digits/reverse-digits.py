class Solution:
	def reverseDigits(self, n):
		# Code here
		rev = 0
		while (n>0):
    		lastDigit = n%10
    		rev = rev * 10+ lastDigit
    		n = n// 10
		return rev