from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        # Product except self is prefix product(self) * postfix product(self)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
        
        return result