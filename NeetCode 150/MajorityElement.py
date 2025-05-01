from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for key, value in hmap.items():
            if value > n // 2:
                return key

        return -1
            
        
        