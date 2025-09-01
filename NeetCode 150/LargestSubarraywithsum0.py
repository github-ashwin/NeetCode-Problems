class Solution:
    def maxLength(self, arr):
        # code here
        max_len = 0
        seen = {}
        prefix_sum = 0
        
        seen[0] = -1
        
        for i in range(len(arr)):
            prefix_sum+=arr[i]
            
            if prefix_sum in seen:
                idx1 = seen[prefix_sum]
                # prefixsum(i) - prefixsum(idx1) = 0
                length = i - idx1
                max_len = max(max_len,length)
            else:
                seen[prefix_sum] = i
                
        return max_len
