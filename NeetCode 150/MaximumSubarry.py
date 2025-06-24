from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -10**4

        currentsum = 0

        for i in range(len(nums)):
            currentsum +=nums[i]
            maxsum = max(maxsum,currentsum)

            if currentsum < 0:
                currentsum=0
        
        return maxsum
        