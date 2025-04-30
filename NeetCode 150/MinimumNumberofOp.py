from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        op = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in seen:
                op = math.ceil((i+1)/3)
                break
            seen.add(nums[i])
        return op