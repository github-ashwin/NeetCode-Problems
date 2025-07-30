from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Bruteforce method

        for left in range(len(heights)):
            for right in range(l+1,len(heights)):
                area = (right-left) * min(heights[left],heights[right])
                result = max(area,result)
        return result

        """
        left = 0
        right = len(heights)-1

        result = 0

        while left < right:
            # Shift pointers based on max. area
            area = (right-left) * min(heights[left],heights[right])
            result = max(area,result)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return result
        
        