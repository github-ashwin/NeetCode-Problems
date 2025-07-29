from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        # Check for the smallest missing number. If it exists, check next(increment)
        for num in nums:
            if num > 0 and missing == num:
                missing +=1
        return missing
        