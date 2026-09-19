class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minp = nums[0]
        maxp = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0:

                temp = maxp
                maxp = minp
                minp = temp
            
            maxp = max(num, num * maxp)
            minp = min(num, num * minp)

            result = max(result, maxp)
        
        return result
        