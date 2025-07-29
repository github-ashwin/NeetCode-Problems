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
    
    """
    Boolean Array method

    n = len(nums)

        seen = [False] * (n+1)

        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        for i in range(1,n+1):
            if seen[i] == False:
                return i
        
        return n+1
        
    """
        