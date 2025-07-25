from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = list(set(sorted(nums)))
        # large = 1
        # seq = 1
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i]+1:
        #         seq+=1
        #     else:
        #         seq = 1
        #     large = max(seq,large)
        # return large

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set: # Identifying the start of sequence - num
                length = 1
                while (num + length) in num_set: # End of sequence is num + length
                    length += 1
                longest = max(length, longest)
        return longest
        