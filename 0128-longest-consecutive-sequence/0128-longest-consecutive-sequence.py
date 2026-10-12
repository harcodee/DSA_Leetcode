
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        arr = sorted(nums)
        counter = 1
        longest = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue

            if arr[i] == arr[i - 1] + 1:
                counter += 1
            else:
                counter = 1

            longest = max(longest, counter)

        return longest
