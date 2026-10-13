class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            prefix_sum += num

            complement = prefix_sum - k
            count += prefix_count.get(complement, 0)

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
        