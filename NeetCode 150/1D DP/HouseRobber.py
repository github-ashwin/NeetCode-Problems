from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0

        for n in nums:
            new_rob = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = new_rob
        
        return rob2
            