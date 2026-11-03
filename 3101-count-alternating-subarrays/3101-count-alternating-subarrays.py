class Solution:
    def countAlternatingSubarrays(self, nums):
        count = 1
        total = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
            else:
                count = 1

            total += count

        return total