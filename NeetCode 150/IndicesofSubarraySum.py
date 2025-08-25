#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        prefix_sum = {0: -1} # Handle edge case
        current_sum = 0
        
        for i,num in enumerate(arr):
            current_sum+=num
            
            if (current_sum-target) in prefix_sum:
                return [prefix_sum[current_sum - target] + 2, i + 1]

            
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
        
        return [-1]
