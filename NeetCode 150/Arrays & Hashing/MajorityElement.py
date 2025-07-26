from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        return max(hm,key=hm.get)