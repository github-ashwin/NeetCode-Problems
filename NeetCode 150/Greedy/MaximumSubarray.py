from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Bruteforce method
        # max_sum = nums[0]
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #     max_sum = max(max_sum,sum)
        # return max_sum

        # Linear method - Kadane's Algorithm
        max_subsum = nums[0] # initial value of the array
        current_sum = 0
        for n in nums:
            if current_sum < 0: # if the prefix becomes 0, eliminate that left num
                current_sum = 0 # reset the current sum
            current_sum +=n # if not, track the current sum
            max_subsum = max(max_subsum,current_sum) # update max
        return max_subsum
