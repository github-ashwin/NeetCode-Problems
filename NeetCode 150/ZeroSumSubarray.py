class Solution:
    def findSubarray(self, arr):
        #code here.
        hm = {}
        count = 0
        prefix_sum = 0
        
        for i in range(len(arr)):
            prefix_sum+=arr[i]
            
            if prefix_sum == 0:
                count+=1
            
            if prefix_sum in hm:
                count+=hm[prefix_sum]
            
            hm[prefix_sum] = hm.get(prefix_sum,0)+1
        
        return count
            
