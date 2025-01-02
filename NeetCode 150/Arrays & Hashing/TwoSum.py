from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     j = i+1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         j = j+1
        
        vals = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in vals:
                return [vals[dif], i] 
            vals[n] = i 
