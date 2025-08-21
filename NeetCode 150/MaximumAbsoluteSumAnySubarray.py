from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        current_max_sum = max_sum = current_min_sum = min_sum = nums[0]

        for i in range(1,len(nums)):

            #Finding the maxsum - Kadane's
            current_max_sum = max(nums[i],current_max_sum+nums[i])
            max_sum = max(max_sum,current_max_sum)

            #Finding the minsum - Kadane's
            current_min_sum = min(nums[i],current_min_sum + nums[i])
            min_sum = min(min_sum,current_min_sum)

        # Since maximum absoulte max_sum will always be > min_sum and we need to find the abs(min_sum)
        return max(max_sum,abs(min_sum))