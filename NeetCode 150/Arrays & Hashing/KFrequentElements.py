from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        """
        We create a bucket list to organize numbers based on their frequencies.
        Each bucket corresponds to a frequency, and all numbers with the same frequency are placed in the same bucket.

        A bucket is an empty list at a specific index of the freq list.
        The index of the bucket corresponds to the frequency of numbers.

        For example:
        If a number appears 3 times, it goes into the bucket at index 3.

        Buckets make it easy to group numbers by frequency.
        """
        
        freq = [[] for i in range(len(nums)+1)] 
        
        for num,c in count.items():
            freq[c].append(num)
        
        res = []

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

