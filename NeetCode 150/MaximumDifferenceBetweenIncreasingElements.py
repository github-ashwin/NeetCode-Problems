from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        diff = -1
        min_idx = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[min_idx]:
                diff = max(diff,nums[i]-nums[min_idx])
            else:
                min_idx = i
                
        return diff

        