from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Set pointers
        left = 0
        right = len(numbers)-1

        while left < right: # Predefined condition
            if numbers[left] + numbers[right] > target:
                right-=1
            elif numbers[left] + numbers[right] < target:
                left+=1
            else:
                return [left+1,right+1]
        return [] # Default
        

        