from typing import List
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                result.append(nums[i:j+1])
        result = [i for i in result if len(i)==3]
        count = 0
        for sub in result:
            if sub[0]+sub[2] == sub[1]/2:
                count+=1
            
        return count