class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i in range(0, len(nums) + 1):
            if freq.get(i, 0) == 0:
                return i