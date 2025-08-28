# from typing import List
# class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums) - k]

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-n for n in nums] # invert values
        heapq.heapify(maxheap)

        for i in range(k-1):
            - heapq.heappop(maxheap)
        
        return -heapq.heappop(maxheap)
        
