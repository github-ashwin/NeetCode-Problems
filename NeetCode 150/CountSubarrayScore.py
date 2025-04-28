from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # subarrays = []
        # for i in range(0,len(nums)):
        #     for j in range(i,len(nums)):
        #         subarrays.append(nums[i:j+1])
        # count = 0
        # for sub in subarrays:
        #     if sum(sub)*len(sub) < k and len(sub)>0:
        #         count +=1
        
        # return count
        
        left = 0
        right = 0
        count = 0
        current = 0

        for right in range(len(nums)):
            current += nums[right]
            while(right-left + 1)*current >= k:
                current-=nums[left]
                left+=1
            else:
                count +=right-left +1
        return count