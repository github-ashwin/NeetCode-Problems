from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Works only if the list is sorted

        i,j = 0,len(nums)-1
        while i<j:
            if nums[i] + nums[j] == target:
                return [i,j]
            elif nums[i] + nums[j] > target:
                j-=1
            else:
                i+=1
        """
        hm = {} # Hashmap for storing key-value pair

        for idx,val in enumerate(nums): # Enumerate through the list
            req = target - val # Checks if the required second number is there in the hashmap already
            if req in hm:
                return[hm[req],idx] # If there, return the current index and the index of second number
            else:
                hm[val]=idx # Else, add the number into the hashmap
        

