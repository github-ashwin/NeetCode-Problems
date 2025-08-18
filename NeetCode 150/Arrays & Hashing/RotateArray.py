from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[-k%len(nums):] - takes last k elements
        # nums[:-k%len(nums)] - takes rest of the list excluding last k
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
       