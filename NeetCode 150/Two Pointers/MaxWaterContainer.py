from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        result = 0

        while left < right:
            val = min(heights[left],heights[right])*(right-left)
            result = max(result,val)

            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        
        return result
        