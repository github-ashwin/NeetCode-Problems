from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def find_pair(limit):
            count=0
            i=0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=limit:
                    count+=1
                    i+=2
                else:
                    i+=1
            return count>=p

        start=0
        stop=nums[-1]-nums[0]
        result=stop

        while start<=stop:
            mid = (start+stop)//2
            if find_pair(mid):
                result = mid
                stop = mid-1
            else:
                start = mid+1
                
        return result



        