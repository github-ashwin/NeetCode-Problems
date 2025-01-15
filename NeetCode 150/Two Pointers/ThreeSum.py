from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                sum = val + nums[p1] + nums[p2]
                if sum > 0:
                    p2 -= 1
                elif sum < 0:
                    p1 += 1
                else:
                    result.append([val, nums[p1], nums[p2]])
                    
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    
                    p1 += 1
                    p2 -= 1

        return result
