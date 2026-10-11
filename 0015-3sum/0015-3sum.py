class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate second elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third elements
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result

        result = set()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if(nums[i] != nums[j] and nums[j] != nums[k]):
                        if (nums[i]+nums[j]+nums[k]==0):
                            triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                            result.add(triplet)
    
        return [list(triplet) for triplet in result]
        