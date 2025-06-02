from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetsum = sum(nums)
        if targetsum%2==0:
            targetsum = targetsum//2
            if sum(nums)-targetsum==targetsum:
                return True
            else:
                return False
        else:
            return False
        