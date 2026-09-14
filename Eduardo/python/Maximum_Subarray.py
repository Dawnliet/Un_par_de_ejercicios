class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxim = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):

            current = max(nums[i], nums[i] + current)

            maxim = max(maxim, current)
        return maxim