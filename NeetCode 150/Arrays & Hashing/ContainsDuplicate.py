from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)): # Set contains only distinct elements
            return False
        else:
            return True
         