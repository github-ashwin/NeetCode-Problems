"""
        We create a bucket list to organize numbers based on their frequencies.
        Each bucket corresponds to a frequency, and all numbers with the same frequency are placed in the same bucket.

        A bucket is an empty list at a specific index of the freq list.
        The index of the bucket corresponds to the frequency of numbers.

        For example:
        If a number appears 3 times, it goes into the bucket at index 3.

        Buckets make it easy to group numbers by frequency.
"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the occurances
        seen = {}
        bucket = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        
        for num, count in seen.items(): # Bucket sort technique [count:number format]
            bucket[count].append(num)

        result = []
        for i in range(len(bucket)-1,0,-1): # Getting the most frequent elements (descending order)
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result


        
        
        
        

