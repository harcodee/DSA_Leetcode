class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = {}
        list=[]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, count in freq.items():
            if count > n // 3:
                list.append(num)
        return list
                