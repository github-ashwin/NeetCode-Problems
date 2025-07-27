from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3 # Counting sort method
        for num in nums:
            count[num]+=1
        
        index = 0

        for i in range(3):
            while count[i]:
                count[i]-=1 # Reduce count
                nums[index]=i # Change the item in the org. list
                index+=1 # Change index
            

        